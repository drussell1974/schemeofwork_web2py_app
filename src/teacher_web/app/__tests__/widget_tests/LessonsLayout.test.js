import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../../helpers/domManipulators';
import FakeApiService from '../../helpers/FakeApiService';

import { LessonsPageLayout } from '../../pages/Lessons';

describe('LessonsLayout', () => {
    let render, container;
    let schemesofwork, lessons;

    const getLeftColumm = function() {
        return container.querySelector("div.container > div.col-lg-4, div.col-md-4");
    }

    const getMainContent = function() {
        return container.querySelector("div.container > div.col-lg-8, div.col-md-10, div.mx-auto");
    }

    beforeEach(() => {
        (
            { render, container } = createContainer()
        )
    })

    it('renders empty content', () => {
        render(<LessonsPageLayout />);

        expect(
            getLeftColumm().textContent
        ).toEqual('');

        expect(
            getMainContent().textContent
        ).toEqual('');
    })

    it('has two columns', () => {
        render(<LessonsPageLayout schemesOfWork={[]} lessons={[]}/>);

        expect(
            getLeftColumm()
        ).not.toBeNull();

        expect(
            getMainContent()
        ).not.toBeNull();
    })

    it('has schemes of work in sidebar', () => {
        
        schemesofwork = FakeApiService.getSchemesOfWork();
        
        render(
            <Router>
                <LessonsPageLayout schemesOfWork={schemesofwork} />
            </Router>);

        expect(
            getLeftColumm().querySelectorAll("ul > li.nav-item")
        ).toHaveLength(3);
    })

    it('has lessons in main content', () => {
        
        lessons = FakeApiService.getLessonEpisodes();
        
        render(
            <Router>
                <LessonsPageLayout lessons={lessons} />
            </Router>);

        expect(
            getMainContent().querySelectorAll(".post-preview")
        ).toHaveLength(4);
    })
})