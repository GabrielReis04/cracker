self.addEventListener('install', function(event) {
    console.log('Service Worker instalando.');
    // Cache arquivos aqui se necessário
  });
  
  self.addEventListener('fetch', function(event) {
    console.log('Fetching:', event.request.url);
    // Controle as requisições aqui
  });
  