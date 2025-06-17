class Solution {
    public boolean judgeCircle(String moves) {
        int left=0,right=0,up=0,down=0;
        int i=0;
        while (i<moves.length()){
            char move=moves.charAt(i);
            switch(move){
                case 'R':
                    right+=1;
                    break;
                case 'L':
                    left+=1;
                    break;
                case 'U':
                    up+=1;
                    break;
                case 'D':
                    down+=1;
                    break;
            }
        i++;
        }
    return up == down && right == left;
    }
}