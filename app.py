import streamlit as st
from datetime import datetime, date
import random

# Configuração
st.set_page_config(page_title="BARGEND | Grátis", page_icon="✂️")

# --- BANCO DE DADOS (Persistente enquanto o site estiver aberto) ---
if 'agenda' not in st.session_state:
    st.session_state.agenda = []

# --- CONFIGURAÇÕES ---
SENHA_ADM = "ramos657"
UNIDADES = {
    "Unidade 1 - Bairro Ipê": ["Thailo", "Jefferson", "Junior"],
    "Unidade 2 - Bairro Boa Vista": ["Davi", "Cabral"]
}

st.title("✂️ BARGEND")

# --- INTERFACE DE AGENDAMENTO ---
tab1, tab2, tab3 = st.tabs(["📅 Agendar", "🛍️ Loja", "⚙️ Painel ADM"])

with tab1:
    with st.form("agendar"):
        unidade = st.selectbox("Unidade", list(UNIDADES.keys()))
        barbeiro = st.selectbox("Barbeiro", UNIDADES[unidade])
        data = st.date_input("Data", min_value=date.today())
        hora = st.selectbox("Hora", ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"])
        nome = st.text_input("Seu Nome")
        
        btn = st.form_submit_button("CONFIRMAR AGENDAMENTO")
        
        if btn:
            if nome:
                id_agend = random.randint(1000, 9999)
                agendamento = {
                    "id": id_agend, "cliente": nome, "unidade": unidade, 
                    "barbeiro": barbeiro, "data": str(data), "hora": hora, "status": "Confirmado"
                }
                st.session_state.agenda.append(agendamento)
                
                st.success(f"✅ FEITO! Horário reservado. ID: {id_agend}")
                st.balloons()
                
                # COMO É 100% GRÁTIS:
                # O sistema mostra o resumo aqui. Você deixa o Painel ADM aberto
                # no seu celular/PC e ele atualiza na hora com o novo agendamento.
            else:
                st.error("Digite seu nome para confirmar.")

with tab2:
    st.write("### Itens Disponíveis")
    st.info("Consulte a disponibilidade com o barbeiro no momento do atendimento.")
    st.write("- Pomadas\n- Shampoos\n- Óleos")

with tab3:
    senha = st.text_input("Senha Master", type="password")
    if senha == SENHA_ADM:
        st.subheader("📋 Agenda de Hoje")
        if st.session_state.agenda:
            # Exibe os agendamentos de forma organizada
            for item in st.session_state.agenda:
                st.write(f"**ID {item['id']}** - {item['cliente']} às {item['hora']} ({item['barbeiro']})")
        else:
            st.write("Nenhum agendamento ainda.")
