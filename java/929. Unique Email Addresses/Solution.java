import java.util.Set;
import java.util.HashSet;

class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> uniqueEmails = new HashSet<>();

        for (String email : emails) {
            String[] tmp = email.split("@");
            String local = tmp[0], domain = tmp[1];
            local = local.split("\\+")[0];
            local = local.replace(".", "");
            uniqueEmails.add(local + "@" + domain);
        }

        return uniqueEmails.size();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.numUniqueEmails(new String[]{"test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"}));
    }
}