document.addEventListener('DOMContentLoaded', function () {
    const cartCount = document.getElementById('cart-count');
    const productModalLabel = document.getElementById('productModalLabel');
    const productModalBody = document.querySelector('.modal-body');
    const forms = document.querySelectorAll('.form-container');
    
    // Example product descriptions
    const productDescriptions = {
        "Apple iPhone 15 Pro Max": "The latest and greatest from Apple. Features a 6.7-inch display, A17 Bionic chip, and a triple-lens camera system.",
        "Samsung Galaxy S24 Ultra": "Samsung's flagship with a 6.8-inch display, Exynos 2400 processor, and a quad-lens camera system.",
        "Google Pixel 9 Pro XL": "Google's top model with a 6.7-inch OLED display, Tensor G3 chip, and advanced computational photography features.",
        "Apple iPhone 14 Pro Max": "High-end Apple smartphone with a 6.7-inch display, A16 Bionic chip, and a triple-lens camera system.",
        "Apple iPhone 15 Pro": "Smaller version of the iPhone 15 Pro Max with the same powerful A17 Bionic chip and camera system.",
        "Google Pixel 9 Pro": "Google's slightly smaller flagship with a 6.3-inch OLED display, Tensor G3 chip, and great photography features."
    };

    // Event listener for product modal
    document.querySelectorAll('.learn-more').forEach(link => {
        link.addEventListener('click', function () {
            const productName = this.dataset.product;
            productModalLabel.textContent = productName;
            productModalBody.innerHTML = `<p>${productDescriptions[productName]}</p>`;
        });
    });

    // Event listener for add to cart
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function () {
            let count = parseInt(cartCount.textContent) || 0;
            count += 1;
            cartCount.textContent = count;
            alert(`${this.dataset.product} added to cart!`);
        });
    });

    // Function to show specific form
    function showForm(formId) {
        forms.forEach(form => form.classList.remove('active'));
        document.getElementById(formId).classList.add('active');
    }

    // Function to hide all forms
    function hideForms() {
        forms.forEach(form => form.classList.remove('active'));
    }

    // Event listener for form submission
    document.getElementById('account-form')?.addEventListener('submit', function (event) {
        event.preventDefault();
        alert('Account created successfully!');
    });

    document.getElementById('signin-form')?.addEventListener('submit', function (event) {
        event.preventDefault();
        alert('Signed in successfully!');
    });

    // Event listener for Google Sign-In button
    document.getElementById('google-signin-btn')?.addEventListener('click', function () {
        alert('Google Sign-In functionality coming soon!');
    });

    // Expose showForm and hideForms functions globally
    window.showForm = showForm;
    window.hideForms = hideForms;
});
