import pickle

files = "Data/profile.pickle"
profile = {"이름":"박명수", "나이":30, "취미": ["축구", "골프", "코딩" ]}

# profile_file = open(files,"wb")
# print(profile)

# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open(files, "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

with open(files, "wb") as f:
    pickle.dump(profile, f)

with open(files, "rb") as f:
    data = pickle.load(f)

print(data)
 