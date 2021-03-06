import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';

import { LessonsBoxMenuItem } from '../widgets/LessonsBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let lesson = {
    id: 1,
    institute_id: 5,
    department_id: 2,
    title: "Curabitur id purus feugiat, porttitor.",
    summary: "In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus",
    image_url: "images/pic01.jpg",
    url: "https://youtu.be/s6zR2T9vn2a",
    number_of_learning_objectives:5,
    number_of_resources:2
}

describe ('LessonsBoxMenuItem', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
                <LessonsBoxMenuItem />
            </MemoryRouter>
            );

        expect(container.textContent).toMatch('');
    })

    it('has a link from image', () => {
        render(
            <MemoryRouter>
                <LessonsBoxMenuItem data={lesson} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.box a').getAttribute('href')
        ).toMatch('https://youtu.be/s6zR2T9vn2a');
    })

    it('has a image', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuItem  data={lesson} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic01.jpg');
    })

    it('has a title', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuItem  data={lesson} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner h3').textContent
        ).toMatch('Curabitur id purus feugiat, porttitor.');
    })

    it('has a summary', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuItem  data={lesson} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner p').textContent
        ).toMatch('In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus');
    })

    it('has a view button', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuItem data={lesson} typeButtonText='View' typeButtonClass="button style2 fit" />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner a.button').textContent
        ).toMatch('View');

        expect(
            container.querySelector('div.inner a.button').getAttribute('href')
        ).toMatch('/lesson');
    })

    it('has type label heading', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuItem data={lesson} typeLabelText="lesson" />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner label.label').textContent
        ).toMatch('lesson');
    })
})