const formulario = document.getElementById('formulario-prospeccion');
const botonEnviar = document.getElementById('boton-enviar');
const estadoCarga = document.getElementById('estado-carga');
const resultadoTarjeta = document.getElementById('resultado-tarjeta');
const correoTexto = document.getElementById('correo-texto');

formulario.addEventListener('submit', async (e) => {
    e.preventDefault();

    const nichoValor = document.getElementById('nicho').value;
    const presupuestoValor = parseInt(document.getElementById('presupuesto').value);

    botonEnviar.disabled = true;
    botonEnviar.classList.add('opacity-50', 'cursor-not-allowed');
    estadoCarga.classList.remove('hidden');
    resultadoTarjeta.classList.add('hidden');

    try {
        const respuesta = await fetch('http://127.0.0', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nicho: nichoValor,
                presupuesto_base: presupuestoValor
            })
        });

        if (!respuesta.ok) {
            throw new Error(`Error en el servidor: ${respuesta.status}`);
        }

        const data = await respuesta.json();

        correoTexto.textContent = data.correo_generado;
        resultadoTarjeta.classList.remove('hidden');

    } catch (error) {
        alert(`Hubo un problema al ejecutar los agentes: ${error.message}`);
        console.error(error);
    } finally {
        botonEnviar.disabled = false;
        botonEnviar.classList.remove('opacity-50', 'cursor-not-allowed');
        estadoCarga.classList.add('hidden');
    }
});