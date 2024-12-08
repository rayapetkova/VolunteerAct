const lightLogo = document.currentScript.getAttribute('lightLogo')
const darkLogo = document.currentScript.getAttribute('darkLogo')

const headerElement = document.getElementsByTagName('header')[0]
const imgLogoAElement = document.getElementsByClassName('img-logo')[0]
const imageLogo = imgLogoAElement.getElementsByTagName('img')[0]

const signInAElement = document.querySelector('.sign-in-li a')
const contactUsAElement = document.querySelector('.contact-us a')
const aboutUsAElement = document.querySelector('.about-us a')

const allEventsLiElement = document.getElementsByClassName('all-events')[0]
let allEventsAElement = null
if (allEventsLiElement) {
    allEventsAElement = allEventsLiElement.getElementsByTagName('a')[0]
}

const favouritesLiElement = document.getElementsByClassName('favourite-events')[0]
let favouritesAElement = null
if (favouritesLiElement) {
    favouritesAElement = favouritesLiElement.getElementsByTagName('a')[0]
}

const ticketsLiElement = document.getElementsByClassName('tickets-events')[0]
let ticketsAElement = null
if (ticketsLiElement) {
    ticketsAElement = ticketsLiElement.getElementsByTagName('a')[0]
}

const myEventsLiElement = document.getElementsByClassName('my-events')[0]
let myEventsAElement = null
if (myEventsLiElement) {
    myEventsAElement = myEventsLiElement.getElementsByTagName('a')[0]
}

document.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        headerElement.style.backgroundColor = 'rgba(67, 79, 98, 0.76)'
        imageLogo.src = lightLogo

        if (allEventsAElement) {
            allEventsAElement.style.color = '#FFFFFFFF'
        }
        if (favouritesAElement) {
            favouritesAElement.style.color = '#FFFFFFFF'
        }
        if (ticketsAElement) {
            ticketsAElement.style.color = '#FFFFFFFF'
        }
        if (myEventsAElement) {
            myEventsAElement.style.color = '#FFFFFFFF'
        }
        if (signInAElement) {
            signInAElement.style.color = '#FFFFFFFF'
        }
        if (contactUsAElement) {
            contactUsAElement.style.color = '#FFFFFFFF'
        }
        if (aboutUsAElement) {
            aboutUsAElement.style.color = '#FFFFFFFF'
        }
    } else {
        headerElement.style.backgroundColor = 'transparent'
        imageLogo.src = darkLogo

        if (allEventsAElement) {
            allEventsAElement.style.color = '#203069'
        }
        if (favouritesAElement) {
            favouritesAElement.style.color = '#203069'
        }
        if (ticketsAElement) {
            ticketsAElement.style.color = '#203069'
        }
        if (myEventsAElement) {
            myEventsAElement.style.color = '#203069'
        }
        if (signInAElement) {
            signInAElement.style.color = '#203069'
        }
        if (contactUsAElement) {
            contactUsAElement.style.color = '#203069'
        }
        if (aboutUsAElement) {
            aboutUsAElement.style.color = '#203069'
        }
    }
})