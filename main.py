import streamlit as st
import requests
from time import sleep

# URL de la API en Azure
API_URL = "https://deeralebackend.azurewebsites.net"

def cargar_datos_api():
    with st.spinner('Como el plan de azure es el gratuito esto puede tardar un poco la primera vez, ten paciencia por favor...'):
        try:
            # Realiza la solicitud a la API en Azure
            response = requests.get(API_URL)
            # Comprueba si la solicitud fue exitosa
            if response.status_code == 200:
                # Indica que los datos se han cargado
                st.session_state['data_loaded'] = True
                return response.json()
            else:
                st.error("Error al cargar datos desde la API. Por favor, inténtalo de nuevo más tarde.")
                return None
        except requests.RequestException as e:
            st.error(f"Se produjo un error al conectar con la API: {e}")
            return None

def main():
    st.title("Usamos el plan básico de azure, esto puede tardar un poco")

    # Muestra un botón para iniciar la carga de datos desde la API
    if st.button("Cargar datos de la API"):
        data = cargar_datos_api()
        # Si los datos se cargaron correctamente, redirige a la documentación
        if data is not None:
            st.session_state['data_loaded'] = True

    # Redireccionamiento automático si los datos están cargados
    if 'data_loaded' in st.session_state and st.session_state['data_loaded']:
        # Redireccionamiento a la URL de la documentación
        st.markdown('<meta http-equiv="refresh" content="0;url=https://deeralebackend.azurewebsites.net/docs" />', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
