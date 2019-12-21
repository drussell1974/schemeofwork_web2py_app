import React from 'react';
import { SOWBoxMenuWidget } from '../widgets/SOWBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import { getSchemeOfWork, getLessons, getSocialMediaLinks } from '../services/apiReactServices';

class Index extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Lessons: [],
            hasError: false,
        }
    
        this.socialmediadata = [];
    }

    componentDidMount() {

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemeOfWork(this);

        getLessons(this);
    }
    
    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
      }

    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        console.log(error, errorInfo);
        
        this.state = {
            hasError: true,
        }
      }
      
    render() {
        return (
            <React.Fragment>
                 
                <BannerWidget heading={this.state.SchemeOfWork.name} description={this.state.SchemeOfWork.description} />
                    <div id="main">
                        <div className="inner">
                            <SOWBoxMenuWidget data={this.state.Lessons} typeLabelText="Lesson" typeButtonText="View Lesson" />
                        </div>
                    </div>
                <FooterWidget heading="Computer Science SOW" summary='' socialmedia={this.socialmediadata} />

            </React.Fragment>
        )
    }
};

export default Index;