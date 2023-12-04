// detect events on add-to-cart button
document.querySelector('#add-to-cart').addEventListener('click', function() {
    // get product id
    var product_id = this.getAttribute('product_id');

    // send AJAX request to add_to_cart
    fetch('/photostore/add-to-cart/product_id=' + product_id +' /')
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            displayNotificationBanner();
            window.location.href = '/photostore/products/';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function displayNotificationBanner() {
    document.querySelector('.notification').style.display = 'block';
    setTimeout(function() {
        document.querySelector('.notification').style.opacity = '0';
    }, 2000);
}