export class Logger {
    private static instance: Logger;
    private logLevel: 'debug' | 'info' | 'warn' | 'error' = 'info';
  // 로거 레벨을 직접 설정할수 있도록 함

    private constructor() {} // 생성자 : 인스턴스 생성 및 초기화 시킴.
  // 싱글톤 패턴
  // 인스턴스가 없으면 생성하고 있으면 반환
  
    static getInstance(): Logger {
    
      if (!Logger.instance) {
        Logger.instance = new Logger();
      }
      return Logger.instance;
    }
  
    setLogLevel(level: 'debug' | 'info' | 'warn' | 'error') {
      this.logLevel = level;
    }
  
    debug(message: string, ...args: any[]) {
      if (process.env.NODE_ENV === 'development') {
        console.debug(`[DEBUG][${new Date().toISOString()}] ${message}`, ...args);
      }
    }
  
    info(message: string, ...args: any[]) {
      console.info(`[INFO][${new Date().toISOString()}] ${message}`, ...args);
    }
  
    warn(message: string, ...args: any[]) {
      console.warn(`[WARN][${new Date().toISOString()}] ${message}`, ...args);
    }
  
    error(message: string, ...args: any[]) {
      console.error(`[ERROR][${new Date().toISOString()}] ${message}`, ...args);
    }
  }
  
  export const logger = Logger.getInstance();