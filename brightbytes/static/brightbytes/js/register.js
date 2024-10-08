document.addEventListener('DOMContentLoaded', () => {
    validatePasswordStrength();
    validateUsername();
    confirmPassword();
  
    document.querySelector('form').addEventListener('submit', (event) => {
      event.preventDefault();
      validateForm(event);
    });
  
    const capitalizeFirstLetter = (str) => {
      return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
    };
  
    const firstName = document.querySelector('.firstname');
    firstName.addEventListener('input', () => {
      firstName.value = capitalizeFirstLetter(firstName.value);
    });
  
    const lastName = document.querySelector('.lastname');
    lastName.addEventListener('input', () => {
      lastName.value = capitalizeFirstLetter(lastName.value);
    });
  
    const password = document.querySelector('.password');
    password.addEventListener('input', () => {
      isPasswordConfirmed()
        ? (document.querySelector('.confirm').style.color = '#3ec70b')
        : (document.querySelector('.confirm').style.color = '#212529');
    });
  });
  
  const validateUsername = () => {
    const username = document.querySelector('.username');
  
    username.addEventListener('focus', () => {
      document.querySelector('.username-help').classList.remove('d-none');
    });
  
    username.addEventListener('blur', () => {
      document.querySelector('.username-help').classList.add('d-none');
    });
  
    username.addEventListener('input', () => {
      username.value = username.value.toLowerCase().trim();
  
      username.value.length >= 3 && username.value.length <= 16
        ? (document.querySelector('.user-count').style.color = '#3ec70b')
        : (document.querySelector('.user-count').style.color = '#212529');
  
      hasSymbol(username.value)
        ? (document.querySelector('.user').style.color = '#f00')
        : (document.querySelector('.user').style.color = '#3ec70b');
  
      if (username.value.length === 0) {
        document.querySelector('.user').style.color = '#212529';
      }
    });
  };
  
  const validateForm = (e) => {
    const confirmPassword = document.querySelector('.confirm-password');
    const password = document.querySelector('.password');
    const username = document.querySelector('.username');
    let isFormValid = true;
  
    // Remove the invalid input fields
    document.querySelectorAll('.input-frame').forEach((input) => {
      input.classList.remove('is-invalid');
    });
  
    // Hide every invalid feedback
    document.querySelectorAll('.error-message').forEach((el) => {
      if (!el.classList.contains('d-none')) {
        el.classList.add('d-none');
      }
    });
  
    // Ensure no input field is empty
    document.querySelectorAll('.input-frame').forEach((input) => {
      if (input.value.length === 0) {
        const inputName = input.classList[0];
  
        if (inputName === 'firstname' || inputName === 'lastname') {
          errorContainer = document.querySelector('.names-empty');
          errorContainer.style.display = 'block';
        } else {
          errorContainer = document.querySelector(`.${inputName}-empty`);
        }
  
        formErrorRender(input, errorContainer, 'Every input field is required');
        isFormValid = false;
      }
    });
  
    if (!isFormValid) return;
  
    // Define isPasswordInvalid as list because it creates a very long, unreadable if statement
    const isPasswordInvalid = [
      password.value.length < 8,
      password.value.length > 16,
      !hasLowerCase(password.value),
      !hasUpperCase(password.value),
      !hasNumber(password.value),
      !hasSymbol(password.value),
    ];
  
    // Ensure password is valid
    isPasswordInvalid.forEach((element) => {
      if (element === true) {
        const errorContainer = document.querySelector('.password-invalid');
        formErrorRender(password, errorContainer, 'Password is invalid**');
        isFormValid = false;
      }
    });
  
    // Exit if some input is empty of password invalid
    // This works but is not the best solution
    // I will improve this later
    if (!isFormValid) return;
  
    // Ensure username is valid
    if (
      username.value.length < 3 ||
      username.value.length > 16 ||
      hasSymbol(username.value)
    ) {
      formErrorRender(username, errorContainer, 'Username is invalid**');
      return false;
    }
  
    // Ensure password matches
    if (password.value !== confirmPassword.value) {
      const errorContainer = document.querySelector('.confirm-password-invalid');
      formErrorRender(
        confirmPassword,
        errorContainer,
        'Password does not match**'
      );
      return false;
    }
  
    sendFormDataToServer('/register/', '/');
  };
