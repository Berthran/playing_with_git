# 10 Helpful Flags to Use with git log command

1. git log

<p>This command lists all the commits you have in your repository with the following information (commit SHA, date, author email, username and commit message) but in the current branch you’re in</p>

2. git log --oneline

<p>The --oneline flag lists all the commits as git log does, but just in one line with the first 7 characters SHA + the commit message as shown above in the image.,</p>
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--CGOeUo3d--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/tnhnixwlt7rk81528ryb.JPG" />

3. git log --oneline --all
<p>This command lists all the commits that are not yet merged in our main branch, usually from other local branches, current branch commits + other branches commits</p>
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--P4GgUT1J--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/7f39e2lpuq5gpkso2dc7.JPG"/>


4. git log --merges 

5. git log --patch
<p>There is a shorthand for this command which is –p, what this flag actually does is just listing the commits as git log does, but with the changes happened in this commit as well, the + sign means the additional lines of code added to the file/s in this commit, – sign shows the removed parts of code from the file/s in this commit and the white text means it's kept as it is, no changes happen to it.</p>

6. git log --stat
<p>Stat stands for statistics, it lists all the commits with the files and the exact number of changes that happened in each file</p>

7. git log –S”<string>”
<p>This flag is wonderful, it helps you to search for a specific text inside your files, let’s say you search about some names you put on an HTML file and you want to know in how many commits these names reside.</p>

8. git log --grep="value here"
<p>This flag helps a lot if you want to search for a specific commit in terms of a commit message, just put your piece of text you want to search for in commit messages and all the commits match the piece of text you provided will be listed.</p>

9. git log --author=”username or email”
<p>Sometimes you might want filtering commits by author username or email because author here means his username or his email, so you could put one of them in between quotes as a string value, you can also search for two authors in the same time with OR operator in the following format:</p>
<p>git log --author=”username1\|username2”</p.
<p>We used slash here as an escape character, because we're dealing with a string and this last one should be provided or the OR | operator will be considered as one character of the whole username, as in any programming languages like JavaScript especially in RegExp.</p>

10. git log -<n>
<p>should be replaced by a number in order to list the most recent commits, consider the following command git log -3, this one will list the most three recent commits.</p>

11. git log --file1
<p>You can also list commits by files, for example, git log -- index.html you can add multiple files, git log -- index.html script.sh, and this last command lists all the commits that track the changes in these two files index.html and script.html.</p>

12. git  log --graph

13. git log –all –decorate –oneline –graph
