// Mettre à jour le compteur de caractères
function updateCharCount(input, countId) {
    const maxLength = input.getAttribute('maxlength');
    const currentLength = input.value.length;
    const countElement = document.getElementById(countId);
    
    if (countElement) {
        countElement.textContent = currentLength + '/' + maxLength;
        
        // Changer la couleur si on approche de la limite
        if (currentLength >= maxLength * 0.8) {
            countElement.style.color = '#dc3545';
        } else if (currentLength > 0) {
            countElement.style.color = '#007bff';
        } else {
            countElement.style.color = '#6c757d';
        }
    }
}

// Vérifier la force du mot de passe
function checkPassword(input) {
    const password = input.value;
    const strengthBar = document.getElementById('passwordStrength');
    let strength = 'weak';
    
    updateCharCount(input, 'passwordCount');
    
    // Analyser la force du mot de passe
    if (password.length >= 8) {
        let hasUpperCase = /[A-Z]/.test(password);
        let hasLowerCase = /[a-z]/.test(password);
        let hasNumbers = /\d/.test(password);
        let hasSpecialChars = /[!@#$%^&*(),.?":{}|<>]/.test(password);
        
        let strength_count = [hasUpperCase, hasLowerCase, hasNumbers, hasSpecialChars].filter(Boolean).length;
        
        if (strength_count >= 3) {
            strength = 'strong';
        } else if (strength_count >= 2) {
            strength = 'medium';
        }
    }
    
    // Mettre à jour la barre de force
    strengthBar.innerHTML = `<div class="password-strength-bar ${strength}"></div>`;
}

// Gérer la soumission du formulaire
function handleSubmit(event) {
    event.preventDefault();
    
    // Réinitialiser les messages d'erreur
    document.querySelectorAll('.error-message').forEach(el => {
        el.classList.remove('show');
        el.textContent = '';
    });
    
    // Récupérer les valeurs
    const nom = document.getElementById('nom').value.trim();
    const prenom = document.getElementById('prenom').value.trim();
    const email = document.getElementById('email').value.trim();
    const dateNaissance = document.getElementById('dateNaissance').value;
    const genre = document.querySelector('input[name="genre"]:checked');
    const telephone = document.getElementById('telephone').value.trim();
    const adresse = document.getElementById('adresse').value.trim();
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const conditions = document.getElementById('conditions').checked;
    
    let isValid = true;
    
    // Validation NOM
    if (!nom) {
        showError('nomError', 'Le nom est requis');
        isValid = false;
    } else if (nom.length < 2) {
        showError('nomError', 'Le nom doit contenir au moins 2 caractères');
        isValid = false;
    } else if (nom.length > 50) {
        showError('nomError', 'Le nom ne peut pas dépasser 50 caractères');
        isValid = false;
    }
    
    // Validation PRENOM
    if (!prenom) {
        showError('prenomError', 'Le prénom est requis');
        isValid = false;
    } else if (prenom.length < 2) {
        showError('prenomError', 'Le prénom doit contenir au moins 2 caractères');
        isValid = false;
    } else if (prenom.length > 50) {
        showError('prenomError', 'Le prénom ne peut pas dépasser 50 caractères');
        isValid = false;
    }
    
    // Validation EMAIL
    if (!email) {
        showError('emailError', 'L\'email est requis');
        isValid = false;
    } else if (!isValidEmail(email)) {
        showError('emailError', 'Veuillez entrer un email valide');
        isValid = false;
    } else if (email.length > 100) {
        showError('emailError', 'L\'email ne peut pas dépasser 100 caractères');
        isValid = false;
    }
    
    // Validation DATE DE NAISSANCE
    if (!dateNaissance) {
        showError('dateError', 'La date de naissance est requise');
        isValid = false;
    } else {
        const age = calculateAge(new Date(dateNaissance));
        if (age < 13) {
            showError('dateError', 'Vous devez avoir au moins 13 ans');
            isValid = false;
        } else if (age > 120) {
            showError('dateError', 'Veuillez vérifier votre date de naissance');
            isValid = false;
        }
    }
    
    // Validation GENRE
    if (!genre) {
        showError('genreError', 'Veuillez sélectionner un genre');
        isValid = false;
    }
    
    // Validation TELEPHONE (optionnel mais s'il est rempli)
    if (telephone && !isValidPhone(telephone)) {
        showError('telError', 'Veuillez entrer un numéro de téléphone valide');
        isValid = false;
    }
    
    // Validation MOT DE PASSE
    if (!password) {
        showError('passwordError', 'Le mot de passe est requis');
        isValid = false;
    } else if (password.length < 6) {
        showError('passwordError', 'Le mot de passe doit contenir au moins 6 caractères');
        isValid = false;
    } else if (password.length > 30) {
        showError('passwordError', 'Le mot de passe ne peut pas dépasser 30 caractères');
        isValid = false;
    }
    
    // Validation CONFIRMATION MOT DE PASSE
    if (!confirmPassword) {
        showError('confirmError', 'Veuillez confirmer votre mot de passe');
        isValid = false;
    } else if (password !== confirmPassword) {
        showError('confirmError', 'Les mots de passe ne correspondent pas');
        isValid = false;
    }
    
    // Validation CONDITIONS
    if (!conditions) {
        showError('conditionsError', 'Vous devez accepter les conditions d\'utilisation');
        isValid = false;
    }
    
    // Si tout est valide
    if (isValid) {
        showSuccess();
        // Réinitialiser le formulaire après 2 secondes
        setTimeout(() => {
            event.target.reset();
            document.getElementById('successMessage').classList.remove('show');
            document.getElementById('passwordStrength').innerHTML = '';
        }, 3000);
    }
}

// Afficher un message d'erreur
function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    if (errorElement) {
        errorElement.textContent = '❌ ' + message;
        errorElement.classList.add('show');
    }
}

// Afficher un message de succès
function showSuccess() {
    const successElement = document.getElementById('successMessage');
    const nom = document.getElementById('nom').value;
    successElement.textContent = '✅ Inscription réussie! Bienvenue ' + nom + '!';
    successElement.classList.add('show');
}

// Vérifier si l'email est valide
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Vérifier si le téléphone est valide
function isValidPhone(phone) {
    const phoneRegex = /^[\d\s\-\+\(\)]{10,}$/;
    return phoneRegex.test(phone);
}

// Calculer l'âge à partir de la date de naissance
function calculateAge(birthDate) {
    const today = new Date();
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    
    return age;
}

// Initialiser les compteurs de caractères au chargement
window.addEventListener('DOMContentLoaded', () => {
    // Initialiser les compteurs
    const inputsWithCount = [
        { id: 'nom', countId: 'nomCount' },
        { id: 'prenom', countId: 'prenomCount' },
        { id: 'email', countId: 'emailCount' },
        { id: 'adresse', countId: 'adresseCount' },
        { id: 'password', countId: 'passwordCount' }
    ];
    
    inputsWithCount.forEach(item => {
        const input = document.getElementById(item.id);
        if (input) {
            updateCharCount(input, item.countId);
            input.addEventListener('keyup', () => updateCharCount(input, item.countId));
        }
    });
});

// Validation en temps réel
document.addEventListener('DOMContentLoaded', () => {
    // Valider l'email en temps réel
    const emailInput = document.getElementById('email');
    if (emailInput) {
        emailInput.addEventListener('blur', function() {
            const emailError = document.getElementById('emailError');
            if (this.value && !isValidEmail(this.value)) {
                emailError.textContent = '❌ Veuillez entrer un email valide';
                emailError.classList.add('show');
            } else {
                emailError.classList.remove('show');
            }
        });
    }
    
    // Valider le téléphone en temps réel
    const telInput = document.getElementById('telephone');
    if (telInput) {
        telInput.addEventListener('blur', function() {
            const telError = document.getElementById('telError');
            if (this.value && !isValidPhone(this.value)) {
                telError.textContent = '❌ Format de téléphone invalide';
                telError.classList.add('show');
            } else {
                telError.classList.remove('show');
            }
        });
    }
    
    // Vérifier la correspondance des mots de passe
    const confirmPasswordInput = document.getElementById('confirmPassword');
    if (confirmPasswordInput) {
        confirmPasswordInput.addEventListener('keyup', function() {
            const password = document.getElementById('password').value;
            const confirmError = document.getElementById('confirmError');
            
            if (this.value && password !== this.value) {
                confirmError.textContent = '❌ Les mots de passe ne correspondent pas';
                confirmError.classList.add('show');
            } else {
                confirmError.classList.remove('show');
            }
        });
    }
});

console.log('Formulaire d\'inscription chargé avec succès!');
