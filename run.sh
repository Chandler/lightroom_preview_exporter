strings ../catalog.lrcat | python uid_to_name.py > /tmp/uid_to_name.pickle 
cat c/testfiles | xargs python python/test.py
