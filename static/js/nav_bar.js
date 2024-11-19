const lightLogo = document.currentScript.getAttribute('lightLogo')
const darkLogo = document.currentScript.getAttribute('darkLogo')

const headerElement = document.getElementsByTagName('header')[0]
const imgLogoAElement = document.getElementsByClassName('img-logo')[0]
const imageLogo = imgLogoAElement.getElementsByTagName('img')[0]

const signInAElement = document.querySelector('.sign-in-li a')

const favouritesLiElement = document.getElementsByClassName('favourite-events')[0]
const favouritesAElement = favouritesLiElement.getElementsByTagName('a')[0]
const ticketsLiElement = document.getElementsByClassName('tickets-events')[0]
const ticketsAElement = ticketsLiElement.getElementsByTagName('a')[0]

document.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        headerElement.style.backgroundColor = 'rgba(67, 79, 98, 0.76)'
        imageLogo.src = lightLogo
        favouritesAElement.style.color = '#FFFFFFFF'
        ticketsAElement.style.color = '#FFFFFFFF'
        signInAElement.style.color = '#FFFFFFFF'
    } else {
        headerElement.style.backgroundColor = 'transparent'
        imageLogo.src = darkLogo
        favouritesAElement.style.color = '#203069'
        ticketsAElement.style.color = '#203069'
        signInAElement.style.color = '#203069'
    }
})