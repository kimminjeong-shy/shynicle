print('hello mars')
try:
    with open(r'C:/Users/mykim/Downloads/mission_computer_main.log','r',encoding='utf-8') as f:
        for line in f:
          print(line)
except Exception as e:
   print(f'예외발생:{e}')

# 보고서 코딩 
log_path = r'C:/Users/mykim/Downloads/mission_computer_main.log'
trigger_phrase = "2023-08-27 11:35:00,INFO,Oxygen tank unstable."
start_logging = False
log_lines = []
try:
   with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        # 비교할 때만 소문자로 처리
        if not start_logging and trigger_phrase.lower() in line.lower():
            start_logging = True
        if start_logging:
            log_lines.append(line.strip()) 
except Exception as e:
    log_lines.append(f'⚠ 예외 발생: {e}')
with open("log_analysis.md", "w", encoding="utf-8") as report:
    report.write("# 🚀 사고 이후 로그 분석 보고서\n\n")
    report.write("## 🔍 분석 시작 시점\n")
    report.write(f"시작 기준 문장: `{trigger_phrase}`\n\n")
    report.write("## 📄 로그 내용\n\n")
    for line in log_lines:
        report.write(f"- {line}\n")
    report.write("\n---\n\n")
    report.write("✅ 이 보고서는 `oxygen tank unstable` 발생 이후의 로그를 기준으로 자동 생성되었습니다.\n")
    