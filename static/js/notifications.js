console.log("--- DEBUG: Bildirim scripti yüklendi. ---");

const notificationSocket = new WebSocket(
    (window.location.protocol === 'https:' ? 'wss://' : 'ws://') +
    window.location.host +
    '/ws/notifications/'
);

notificationSocket.onopen = function(e) {
    console.log('--- DEBUG: WebSocket bağlantısı başarıyla kuruldu. ---');
};

notificationSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const message = data.message;
    const url = data.url;

    // Bildirimler için bir container oluştur veya bul
    let notificationContainer = document.getElementById('notification-container');
    if (!notificationContainer) {
        notificationContainer = document.createElement('div');
        notificationContainer.id = 'notification-container';
        // Stilini ayarla (sağ üst köşe)
        Object.assign(notificationContainer.style, {
            position: 'fixed',
            top: '80px',
            right: '20px',
            zIndex: '1055',
            display: 'flex',
            flexDirection: 'column',
            gap: '10px'
        });
        document.body.appendChild(notificationContainer);
    }

    // Toast elementini oluştur
    const toastEl = document.createElement('div');
    toastEl.classList.add('toast');
    toastEl.setAttribute('role', 'alert');
    toastEl.setAttribute('aria-live', 'assertive');
    toastEl.setAttribute('aria-atomic', 'true');
    toastEl.style.minWidth = '300px';

    // Toast içeriğini ayarla
    toastEl.innerHTML = `
        <div class="toast-header bg-info text-dark">
            <i class="bi bi-bell-fill me-2"></i>
            <strong class="me-auto">Yeni Bildirim</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            ${message}
        </div>
    `;

    // URL varsa, toast body'yi tıklanabilir yap
    if (url && url !== '#') {
        const toastBody = toastEl.querySelector('.toast-body');
        if (toastBody) {
            toastBody.style.cursor = 'pointer';
            toastBody.addEventListener('click', () => {
                window.location.href = url;
            });
        }
    }
    
    // Toast'ı container'a ekle ve göster
    notificationContainer.appendChild(toastEl);
    const toast = new bootstrap.Toast(toastEl, {
        autohide: false // Bildirimler artık otomatik olarak gizlenmeyecek
    });
    toast.show();

    // Toast gizlendiğinde DOM'dan kaldır
    toastEl.addEventListener('hidden.bs.toast', function () {
        toastEl.remove();
    });
};

notificationSocket.onclose = function(e) {
    console.error('--- DEBUG: WebSocket bağlantısı beklenmedik şekilde kapandı. ---');
};