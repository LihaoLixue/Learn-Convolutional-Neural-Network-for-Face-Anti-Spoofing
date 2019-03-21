import os
def open_file(f=""):
    list_a = []
    if not os.path.exists(f):
        print("File not exists, f is %s!" % f)
        return
    # with open(f, "r+", encoding="utf8") as of:
    with open(f, "r+") as of:
        jsons=of.readlines()
        list_a.append(jsons)
    return list_a
def get_all_together(json_file, job_file, job_topics):
    a = open_file(json_file)
    b = open_file(job_file)
    print(a[0])
    print(b[0])
    c = list(set(a[0])-set(b[0]))
    print(c)
    with open(job_topics, "w") as f_result:
        for i in c:
         f_result.write(i)
if __name__ == "__main__":
    get_all_together("test2.txt", "test1.txt","test.txt")
    # test()