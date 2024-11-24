class AdHocAnalyzer:
    def __init__(self):
        self.s3_client = S3AdhocUtils()
        self.db = Database()
        
    def analyze_error_patterns(self, start_date, end_date):
        """에러 패턴 Ad hoc 분석"""
        try:
            # 1. Ad hoc 쿼리 실행
            query = """
                SELECT 
                    error_type,
                    COUNT(*) as error_count,
                    AVG(response_time) as avg_response_time
                FROM error_logs
                WHERE created_at BETWEEN :start AND :end
                GROUP BY error_type
                HAVING COUNT(*) > 100
            """
            results = self.db.execute_raw_query(query, {
                'start': start_date,
                'end': end_date
            })
            
            # 2. 분석 결과 리포트 생성
            report = {
                'analysis_date': datetime.now().isoformat(),
                'period': f"{start_date} to {end_date}",
                'results': results,
                'summary': self._generate_summary(results)
            }
            
            # 3. S3에 리포트 저장
            report_path = f"reports/adhoc/error_analysis_{datetime.now().strftime('%Y%m%d')}.json"
            self.s3_client.upload(
                content=json.dumps(report),
                name=report_path
            )
            
            return report
            
    def _generate_summary(self, results):
        """분석 결과 요약"""
        return {
            'total_errors': sum(r['error_count'] for r in results),
            'top_error_type': max(results, key=lambda x: x['error_count'])
        }
    