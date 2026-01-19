// Gestion du menu hamburger
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});

// Fermer le menu quand un lien est cliqué
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        updateActiveLink();
    });
});

// Mettre à jour le lien actif de la navigation
function updateActiveLink() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let currentSection = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= sectionTop - 200) {
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').slice(1) === currentSection) {
                link.classList.add('active');
            }
        });
    });
}

updateActiveLink();

// Gestion du formulaire de contact
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const nom = document.getElementById('nom').value;
        const email = document.getElementById('email').value;
        const sujet = document.getElementById('sujet').value;
        const message = document.getElementById('message').value;

        // Validation simple
        if (nom && email && sujet && message) {
            // Afficher un message de succès
            alert(`Merci ${nom}! Votre message a été reçu.\nNous vous répondrons à ${email} très bientôt.\n\nBienvenue chez Nezha Shop!`);
            
            // Réinitialiser le formulaire
            this.reset();
        } else {
            alert('Veuillez remplir tous les champs du formulaire!');
        }
    });
}

// Gestion du formulaire newsletter
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const email = this.querySelector('input[type="email"]').value;
        alert(`Merci! ${email} a été abonnée à notre newsletter.`);
        this.reset();
    });
}

// Animation au défilement
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeIn 0.6s ease-in forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observer les cartes de produits et collections
document.querySelectorAll('.product-card, .collection-card, .testimonial-card').forEach(card => {
    observer.observe(card);
});

// Animation fadeIn
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);

// Boutons d'ajout au panier (simulation)
document.querySelectorAll('.btn-small').forEach(button => {
    if (!button.closest('.collection-image') && !button.closest('.newsletter-form')) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productName = this.closest('.product-card').querySelector('h3').textContent;
            const price = this.closest('.product-footer').querySelector('.price').textContent;
            
            // Créer une animation de confirmation
            const originalText = this.textContent;
            const originalColor = this.style.backgroundColor;
            
            this.textContent = '✓ Ajouté au panier!';
            this.style.backgroundColor = '#388e3c';
            
            console.log(`${productName} (${price}) ajouté au panier!`);
            
            setTimeout(() => {
                this.textContent = originalText;
                this.style.backgroundColor = originalColor;
            }, 2000);
        });
    }
});

// Boutons "Voir collection"
document.querySelectorAll('.collection-image .btn-small').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const collectionName = this.closest('.collection-card').querySelector('h3').textContent;
        alert(`Redirection vers la collection: ${collectionName}`);
    });
});

// Smooth scroll pour tous les liens internes
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// Compteur de produits dans le panier (localStorage)
let cartCount = localStorage.getItem('nezhashop_cartCount') || 0;

function addToCart() {
    cartCount++;
    localStorage.setItem('nezhashop_cartCount', cartCount);
    console.log(`Articles dans le panier: ${cartCount}`);
}

// Animation de parallaxe légère au scroll
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero');
    if (hero) {
        const scrollPosition = window.pageYOffset;
        hero.style.backgroundPosition = `0 ${scrollPosition * 0.5}px`;
    }
});

// Initialiser l'application
console.log('Nezha Shop chargé avec succès! 👑');
