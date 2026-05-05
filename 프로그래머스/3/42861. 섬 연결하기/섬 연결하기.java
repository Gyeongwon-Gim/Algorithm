import java.util.Arrays;

class Solution {
    // 부모 노드를 저장할 배열
    private int[] parent;
    
    // Union-Find: 부모 노드를 찾는 함수
    private int find(int i) {
        if (parent[i] == i){
            return i;
        }
        return parent[i]  = find(parent[i]); // 경로 압축 최적화
    }
    // Union-Find: 두 집합을 합치는 함수
    private void union(int i, int j){
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ)
            parent[rootJ] = rootI;
    }
    
    public int solution(int n, int[][] costs) {
        // 1. 비용을 기준으로 오름차순 정렬
        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));
        // 2. 부모 배열 초기화 (0부터 n-1까지)
        parent = new int[n];
        for (int i = 0; i < n; i++){
            parent[i] = i;
        }
        
        int totalCost = 0;
        int edgeCount = 0;
        
        // 3. 크루스칼 알고리즘 실행
        for (int[] cost : costs) {
            int from = cost[0];
            int to = cost[1];
            int weight = cost[2];
            
            // 사이클이 형성되지 않는 경우에만 연결
            if(find(from) != find(to)) {
                union(from, to);
                totalCost += weight;
                edgeCount++;
                // n개의 섬을 연결하려면 n-1개의 다리가 필요함
                if(edgeCount == n - 1) {
                    break;
                }
            }   
        }
        return totalCost;
    }
}