# PDF 선하증권 파서 (B/L Parser)
선하증권(B/L) PDF 문서에서 중요 정보를 추출하고 구조화된 데이터로 변환하는 프로젝트입니다.
## 주요 기능
- PDF 형식의 선하증권 문서 파싱
- 주요 정보 자동 추출 (선사, 부킹번호, 선박명, ETD/ETA 등)
- ChromaDB를 활용한 문서 임베딩 및 검색
- LLM을 활용한 문서 요약 및 정보 추출
## 기술 스택
- Python 3.12
- LangChain
- Ollama (LLM: Qwen 2.5)
- ChromaDB
- PDFMiner
- Pydantic
## 설치 방법
1. 저장소 클론
```bash
git clone [repository-url]
cd [project-directory]
```
2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
# or
.\venv\Scripts\activate # Windows
```
3. 의존성 설치
```bash
pip install -r requirements.txt
```
4. Ollama 설치 및 모델 다운로드
```bash
ollama pull qwen2.5:14b
ollama pull nomic-embed-text
```
## 사용 방법
1. PDF 파일을 assets 폴더에 위치시킵니다.
2. 메인 프로그램 실행:
```bash
python src/main.py
```
3. 프롬프트에 따라 처리할 PDF 파일 번호를 선택합니다.
## 출력 데이터 구조
추출되는 정보는 다음과 같은 구조를 가집니다:
- carrier: 선사명
- booking_number: 부킹 번호
- feeder_vessel: 피더선박명
- final_vessel: 본선명
- depot: 컨테이너 데포 위치
- port_name: 선적항
- etd: 출항예정일
- eta: 도착예정일
- cargo_closing_date: 화물마감일
- doc_cut_off_date: 서류마감일
- container_type: 컨테이너 타입
- container_quantity: 컨테이너 수량
## 프로젝트 구조
```
.
├── assets/ # PDF 파일 저장 디렉토리
├── src/
│ ├── main.py # 메인 실행 파일
│ ├── model/ # 데이터 모델
│ ├── prompt/ # 프롬프트 템플릿
│ └── service/ # 서비스 로직
├── chroma_db/ # ChromaDB 저장소
└── requirements.txt # 의존성 목록
```
## 라이선스
MIT License
## 기여 방법
1. 프로젝트 포크
```bash
Fork the Project
```
2. 기능 브랜치 생성
```bash
Create your Feature Branch
```
3. Pull Request
```bash
Open a Pull Request
```