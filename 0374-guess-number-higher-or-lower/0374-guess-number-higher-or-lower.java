/** 
 * Forward declaration of guess API.
 * @param num  your guess
 * @return     -1 if num is higher than the target number
 *              1 if num is lower than the target number
 *              0 if num is equal to the target number
 * int guess(int num);
 */

class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1, right = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int res = guess(mid);
            if (res == 0) return mid;
            else if (res < 0) right = mid - 1;
            else left = mid + 1;
        }
        return -1; // should never reach here
    }
}
