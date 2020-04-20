const inputs = document.querySelectorAll('.form-group input');
const labels = document.querySelectorAll('.form-group label');

labels.forEach(label => {
	label.innerHTML = label.innerText
		.split('')
		.map((letter, idx) => `<span style="
				transition-delay: ${idx * 50}ms
			">${letter}</span>`)
		.join('');
});
