import { logger } from '../utils/logger';

const SomeComponent = () => {
  useEffect(() => {
    logger.info('컴포넌트가 마운트되었습니다');
    
    try {
      // 어떤 작업
    } catch (error) {
      logger.error('에러가 발생했습니다:', error);
    }
  }, []);

  return <div>컴포넌트</div>;
};