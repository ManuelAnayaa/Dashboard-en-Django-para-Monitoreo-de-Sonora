// Configuración inicial de la gráfica
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar', // Tipo de gráfica: barra
    data: {
        labels: [], // Aquí irán los nombres (Hermosillo, Guaymas...)
        datasets: [{
            label: 'Temperatura (°C)',
            data: [], // Aquí irán los valores (45, 30...)
            backgroundColor: [
                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: { beginAtZero: true }
        },
        responsive: true
    }
});

// Función para actualizar la gráfica consultando al servidor
function updateChart() {
    fetch('/api/data/')
        .then(response => response.json())
        .then(data => {
            // Limpiamos los datos anteriores
            const municipios = [];
            const valores = [];

            // Procesamos los datos que llegan del MQTT
            for (const [topico, valor] of Object.entries(data)) {
                const partes = topico.split('/'); // sonora/hermosillo/temp
                const municipio = partes[1];

                municipios.push(municipio.charAt(0).toUpperCase() + municipio.slice(1)); // Capitalizar
                valores.push(valor);
            }

            // Actualizamos la gráfica
            myChart.data.labels = municipios;
            myChart.data.datasets[0].data = valores;
            myChart.update();
        })
        .catch(error => console.error('Error actualizando gráfica:', error));
}

// Actualizar cada 3 segundos
setInterval(updateChart, 3000);