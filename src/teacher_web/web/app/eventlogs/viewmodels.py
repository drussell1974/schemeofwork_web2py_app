"""
View Models
"""
import io
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception
from shared.models.core.log_type import LOG_TYPE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel
from shared.models.cls_eventlog import EventLogModel, EventLogFilter


class EventLogIndexViewModel(BaseViewModel):
    
    def __init__(self, db, request, settings, auth_user):

        self.model = []
        self.error_message = ""
        self.settings = settings

        try:
            search_criteria = EventLogFilter()
            
            if request.method == "POST":
                search_criteria.date_from = request.POST["date_from"]
                search_criteria.date_to = request.POST["date_to"]
                search_criteria.type = request.POST["event_type"]
                search_criteria.category = request.POST["category"]
                search_criteria.subcategory = request.POST["subcategory"]

                if request.POST.get("submit", 0) == 2:
                    try:
                        older_than_n_days = try_int(request.POST["days"], return_value=0)
                        
                        if older_than_n_days < settings.MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS:
                            raise Exception("Logs older than %s days cannot be deleted" % settings.MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS)

                        self.model = EventLogModel.delete(db, older_than_n_days, auth_user)

                    except Exception as e:
                        handle_log_exception(db, "Error deleting old event logs", e)
                        self.error_message = e

            self.db = db
            self.auth_user = auth_user
            self.search_criteria = search_criteria

            self.search_criteria.validate()
            
            if search_criteria.is_valid == True:
                self.model = EventLogModel.get_all(self.db, self.search_criteria, self.auth_user)
        except Exception as e:
            self.error_message = e


    def view(self):
        
        data = { 
            "event_type_options": [
                {"key": "Error", "value": LOG_TYPE.Error },
                {"key": "Warning", "value": LOG_TYPE.Warning },
                {"key": "Information", "value": LOG_TYPE.Information },
                {"key": "Verbose", "value": LOG_TYPE.Verbose },
            ],
            "search_criteria": self.search_criteria,
            "event_logs": self.model,
            "settings": self.settings
        } 
        
        return ViewModel("", "Event Log", "view event logs", data=data, error_message=self.error_message)


class EventLogDeleteOldViewModel:
    
    def __init__(self, db, request, settings, auth_user):
        """ delete event log on POST """
        
        self.model = 0

        if request.method == "POST":
            try:
                older_than_n_days = try_int(request.POST["days"], return_value=0)
                
                if older_than_n_days < settings.MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS:
                    raise Exception("Logs older than %s days cannot be deleted" % settings.MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS)

                self.model = EventLogModel.delete(db, older_than_n_days, auth_user)

            except Exception as e:
                handle_log_exception(db, "Error deleting old event logs", e)
                raise