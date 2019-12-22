import React, { Fragment } from 'react';
import BannerWidget from '../widgets/BannerWidget';
import { LatestSchemesOfWorkJumbotronWidget } from '../widgets/LatestSchemesOfWorkJumbotronWidget';

class Index extends React.Component {
    
    render() {
        let latest_schemes_of_work = [];

        return (        
            <Fragment>
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 col-md-8 mx-auto">
                            <LatestSchemesOfWorkJumbotronWidget data={latest_schemes_of_work} />
                        </div>
                    </div>
                </div>
                <hr/>
            </Fragment>
        )
    }
};

export default Index;