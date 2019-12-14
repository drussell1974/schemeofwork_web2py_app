import React from 'react';
import { LessonBoxMenuWidget } from '../widgets/LessonBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';

class Index extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Lessons: [],
            hasError: false,
        }
    
        self.socialmediadata = [];
    }

    componentDidMount() {
        //handleRefresh();
        self.socialmediadata = [
            {
                "name":"Twitter",
                "iconClass":"icon fa-twitter",
                "url":"http://twitter.com",
            },
            {
                "name":"Facebook",
                "iconClass":"icon fa-facebook",
                "url":"http://www.facebook.com",
            },
            {
                "name":"Instagram",
                "iconClass":"icon fa-instagram",
                "url":"http://www.instagram.com",
            },
            {
                "name":"Email",
                "iconClass":"icon fa-envelope",
                "url":"mail://noaddress@example.com",
            },
        ];
        
        fetch("http://127.0.0.1:8000/api/schemeofwork/127?format=json"   )
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                console.log(data);
                this.setState({
                    SchemeOfWork: data.schemeofwork, 
                    hasError: false,
                });
            },  
            (error) => {
                this.setState({
                    SchemeOfWork: {},
                    hasError: true,
                });
            }
        )

        fetch("http://127.0.0.1:8000/api/schemeofwork/127/lessons?format=json"   )
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                console.log(data);
                this.setState({
                    Lessons: data.lessons, 
                    hasError: false,
                });
            },  
            (error) => {
                this.setState({
                    Lessons: [],
                    hasError: true,
                });
            }
        )
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
                
                <BannerWidget data={this.state.SchemeOfWork} />
                
                <div id="main">
                    <div className="inner">
                        <LessonBoxMenuWidget data={this.state.Lessons} />
                    </div>
                </div>

                <FooterWidget heading="Computer Science SOW" summary='' socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
};

export default Index;