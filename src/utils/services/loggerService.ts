interface LogEntry {
    level: string;
    message: string;
    timestamp: string;
    metadata?: any;
  }
  
  export const sendLogsToServer = async (logEntry: LogEntry) => {
    // 로그래벨 전송 함수
    // 로그 서버 주소는 환경변수로 설정 (외부 url)
    // 프로덕션 레벨에서는 console.log 대신 함수 사용
    try {
      const response = await fetch('YOUR_LOG_SERVER_URL', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(logEntry),
      });
      return response.ok;
    } catch (error) {
      console.error('로그 전송 실패:', error);
      return false;
    }
  }
