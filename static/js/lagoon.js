/* Lagoon Solar concept website enhancements: browser-side only, no backend. */
(function () {
  'use strict';
  document.querySelectorAll('img[data-local-fallback]').forEach(function (img) {
    function useFallback() {
      if (img.dataset.fallbackApplied === 'yes') return;
      img.dataset.fallbackApplied = 'yes';
      img.src = img.dataset.localFallback;
    }
    img.addEventListener('error', useFallback, { once: true });
    if (img.complete && img.naturalWidth === 0) useFallback();
  });

  var spinner = document.getElementById('spinner');
  if (spinner) spinner.classList.remove('show');

  var demoAddress = 'hello@lagoonsolar.example';
  document.querySelectorAll('form[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      if (!form.reportValidity()) return;
      var data = new FormData(form);
      var kind = form.dataset.demoForm;
      var client = String(data.get('name') || '').trim();
      var subject = kind === 'quote'
        ? 'Solar power enquiry - ' + String(data.get('service') || 'New request')
        : String(data.get('subject') || 'Website enquiry');
      var body = [
        'Hello Lagoon Solar,', '',
        'My name: ' + client,
        'Email: ' + String(data.get('email') || ''),
        'Phone: ' + String(data.get('phone') || 'Not supplied'),
        'Service: ' + String(data.get('service') || 'General enquiry'), '',
        String(data.get('message') || '').trim(), '',
        '--- Prepared by Lagoon Solar demo form ---'
      ].join('\n');
      var feedback = form.querySelector('.form-feedback');
      if (feedback) {
        feedback.textContent = 'Your email app should open with a pre-filled draft. This demo does not send or store form submissions; replace the sample email with a real address before launch.';
        feedback.classList.add('text-primary');
      }
      window.location.href = 'mailto:' + demoAddress + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  });
})();
