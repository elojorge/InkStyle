# InkStyle Tattoo Platform  

**Repositório**: [InkStyle](https://github.com/elojorge/InkStyle)  
**Status**: Em andamento (🚧 work in progress)  

---

## 🎯 Visão Geral  
A **InkStyle** é uma plataforma web para conectar clientes a tatuadores profissionais, oferecendo:  
- 📅 Agendamento inteligente baseado na agenda do tatuador.  
- 🎨 Geração de arte conceitual via IA (Stable Diffusion ou Midjourney).  
- 💳 Pagamentos seguros com PIX, cartão e PayPal.  
- ⭐ Portfólio interativo e sistema de avaliações.  

![Demo](screenshots/demo.gif) *Interface de agendamento e geração de arte*  

---

## 🛠️ Tecnologias  

| Categoria          | Tecnologias                                                                 |  
|---------------------|-----------------------------------------------------------------------------|  
| **Backend**         | Django, Django REST Framework, Flask (microsserviço de IA)                  |  
| **Frontend**        | React, TypeScript, Bootstrap                                               |  
| **Banco de Dados**  | PostgreSQL, Redis                                                          |  
| **IA**              | Stable Diffusion, Midjourney, PyTorch                                      |  
| **Pagamentos**      | Stripe, Mercado Pago                                                       |  
| **DevOps**          | Docker, GitHub Actions, AWS EC2/S3                                         |  

---

## 📂 Estrutura do Projeto  

```plaintext  
InkStyle/  
├── core/                     # Configurações Django  
├── usuarios/                 # Autenticação e perfis  
├── agendamentos/            # Lógica de agendas e calendário  
├── pagamentos/              # Integração com Stripe/Mercado Pago  
├── ia_artes/                # Microsserviço Flask (geração de IA)  
│   ├── app.py               # Endpoint da IA  
│   └── models/              # Modelos pré-treinados  
├── frontend/                # Aplicação React  
├── Dockerfile               # Configuração de containers  
└── requirements.txt         # Dependências Python


🚀 Funcionalidades
Para Clientes
🔍 Buscar tatuadores por estilo, localização ou avaliação.

🖼️ Gerar arte conceitual com IA a partir de descrições textuais.

📊 Visualizar portfólio e histórico de trabalhos do tatuador.

Para Tatuadores
🗓️ Gerenciar agenda e bloquear horários indisponíveis.

💰 Configurar métodos de pagamento e preços por sessão.

📈 Acompanhar métricas de desempenho (visualizações, conversões).

Para Desenvolvedores
🔄 API RESTful documentada com Swagger.

🤖 Pipeline de CI/CD para deploy automático na AWS.

📦 Microsserviços independentes (Django + Flask).

⚙️ Como Executar
Pré-requisitos
Python 3.10+, Node.js 18+, Docker.

Chaves de API: Stripe, AWS S3, e Stable Diffusion.

Passo a Passo

Clone o repositório:
git clone https://github.com/elojorge/InkStyle.git  
cd InkStyle

Configure o ambiente:
python -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt

Configure as variáveis (.env):
SECRET_KEY=sua_chave_aqui  
STRIPE_API_KEY=sk_test_...  
STABLE_DIFFUSION_KEY=...

Inicie os containers:
docker-compose up -d  # PostgreSQL, Redis

Execute o servidor Django:
python manage.py migrate  
python manage.py runserver

Acesse:

Frontend: http://localhost:3000

API Docs: http://localhost:8000/swagger

📌 Roadmap

| Funcionalidade       | Status        | Prioridade |
|----------------------|---------------|------------|
| Chat integrado       | Em progresso  | Alta       |
| Assinaturas mensais  | Planejado     | Média      |
| App Mobile           | Futuro        | Baixa      |
