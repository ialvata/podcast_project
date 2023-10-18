const imageUrls = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
];

const gallery = document.getElementById('gallery');

imageUrls.forEach((imageUrl) => {
    const image = document.createElement('img');
    image.src = imageUrl;
    image.alt = 'Podcast_Name';
    image.className = 'gallery-item';
    // image.id = ""
    gallery.appendChild(image);
});
