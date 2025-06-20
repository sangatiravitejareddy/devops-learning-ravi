2. Check current file permissions (optional):
bash
CopyEdit
ls -l day6-script.sh

You'll see something like:
css
CopyEdit
-rw-r--r-- 1 ravi ... day6-script.sh

Here, -rw-r--r-- means:
r = read


w = write


❌ no x = executable



3. Add executable permission:
bash
CopyEdit
chmod +x day6-script.sh

Now recheck permissions:
bash
CopyEdit
ls -l day6-script.sh

You should now see:
diff
CopyEdit
-rwxr-xr-x 1 ravi ... day6-script.sh

✅ This means:
Owner can read/write/execute


Group & others can read/execute



4. Run the script using:
bash
CopyEdit
./day6-script.sh

It will execute like a native app.

🧠 What chmod +x Means
chmod = change mode (permissions)


+x = add executable flag


This is required if you want to run a script with ./script.sh instead of bash script.sh
