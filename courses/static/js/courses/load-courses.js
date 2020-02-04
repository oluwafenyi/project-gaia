
const createElement = (elDatum, parent) => {
    const el = document.createElement(elDatum.type);
    if (elDatum.className) {
        el.className = elDatum.className;
    }
    if (elDatum.customAttributes) {
        elDatum.customAttributes.forEach((attr) => {
            const [key, value] = attr;
            el.setAttribute(key, value);
        });
    }
    if (elDatum.textContent) {
        el.textContent = elDatum.textContent;
    }
    if (elDatum.click) {
        el.addEventListener('click', () => {
            window.location.href = elDatum.click;
        });
    }
    if (elDatum.style) {
        el.style = elDatum.style;
    }
    if (elDatum.children) {
        elDatum.children.forEach((child) => {
            createElement(child, el);
        });
    }
    parent.appendChild(el);
    return el;
}

const appendCourse = (course) => {
    const parent = document.getElementById('courseList');

    const elData = [{
        type: 'div',
        className: 'col-12 col-md-6 col-lg-4',
        click: course.url,
        style: 'cursor: pointer;',
        children: [{
            type: 'div',
            className: 'single-popular-course mb-100 wow fadeInUp',
            customAttributes: [
                ['data-wow-delay', '250ms']
            ],
            children: [{
                type: 'div',
                className: 'course-content fixed-course-height',
                children: [{
                        type: 'h5',
                        textContent: `${course.code}: ${course.title}`,
                    },
                    {
                        type: 'div',
                        className: 'meta d-flex align-items-center',
                        children: [
                            ...course.lecturers.map((lecturer) => {
                                return {
                                    type: 'a',
                                    textContent: lecturer,
                                }
                            }),
                            {
                                type: 'span',
                                children: [{
                                    type: 'i',
                                    className: 'fa fa-circle',
                                    customAttributes: [
                                        ['aria-hidden', 'true']
                                    ]
                                }]
                            },
                            {
                                type: 'a',
                                textContent: course.category,
                                customAttributes: [
                                    ['href', '#']
                                ]
                            }
                        ]
                    },
                    {
                        type: 'p',
                        textContent: course.description
                    },
                ]
            },
            {
                type: 'div',
                className: 'seat-rating-fee d-flex justify-content-between',
                children: [
                    {
                        type: 'div',
                        className: 'seat-rating h-100 d-flex align-items-center',
                        children: [
                            {
                                type: 'div',
                                className: 'rating',
                                children: [
                                    {
                                        type: 'i',
                                        className: 'fa fa-star',
                                        customAttributes: [
                                            ['aria-hidden', 'true'],
                                        ],
                                    }
                                ],
                                textContent: `${course.units} Units `,
                            },
                        ],
                    },
                ],
            }, ]
        }, ]
    }, ];

    elData.forEach(element => {
        createElement(element, parent);
    });

};

const loadMore = (pageNumber, query) => {
    let url = document.getElementById('loadMore').getAttribute('api');
    url = url + `?page=${pageNumber}`;
    if (query) {
        url = url + `&query=${query}`;
    }
    return fetch(url)
        .then(response => response.json())
        .then(response => {
            if (!response.next) {
                button.parentNode.removeChild(button);
            }
            response.data.forEach(object => {
                appendCourse(object);
            });
        })
        .catch(error => console.log(error));
};

const button = document.getElementById('loadMore');
const query = window.location.search.substr(1).split('=')[1];
let nextPage = 2;

if (button) {
    button.addEventListener('click', () => {
        loadMore(nextPage, query);
        nextPage++;
    });
}
