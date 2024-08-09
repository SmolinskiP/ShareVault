document.addEventListener('DOMContentLoaded', function () {
    var uploadInput = document.querySelector('.file-upload input[type="file"]');
    var progressBar = document.getElementById('progressBar');
    var status = document.getElementById('status');

    if (uploadInput) {
        uploadInput.addEventListener('change', function () {
            var file = uploadInput.files[0];
            var formData = new FormData();
            formData.append('file', file);

            var xhr = new XMLHttpRequest();
            xhr.open('POST', window.location.href, true);

            xhr.upload.addEventListener('progress', function (e) {
                if (e.lengthComputable) {
                    var percentComplete = (e.loaded / e.total) * 100;
                    progressBar.value = percentComplete;
                    status.innerHTML = Math.round(percentComplete) + '% uploaded';
                }
            }, false);

            xhr.onload = function () {
                if (xhr.status === 200) {
                    status.innerHTML = 'File uploaded successfully!';
                    progressBar.value = 0;
                } else {
                    status.innerHTML = 'Error uploading file.';
                }
            };

            xhr.send(formData);
        });
    }
});

