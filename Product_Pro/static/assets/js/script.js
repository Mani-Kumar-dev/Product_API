document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.view-product-btn').forEach(button => {
        button.addEventListener('click', function () {
            const productId = this.getAttribute('data-id');
            fetch(`product/${productId}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        // Populate modal fields with the product data
                        document.getElementById('modal_product_name').textContent = data.product_name;
                        document.getElementById('modal_description').textContent = data.description;
                        document.getElementById('modal_price').textContent = data.price;
                    }
                })
                .catch(error => console.error('Error fetching product details:', error));
        });
    });
});