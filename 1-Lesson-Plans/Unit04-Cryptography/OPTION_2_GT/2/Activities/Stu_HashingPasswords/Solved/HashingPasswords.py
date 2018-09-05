# Import the hashlib library into the application
import hashlib

# List of sha256 hashed passwords
hashed_passes = [
  '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92',
  '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
  'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f',
  '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',
  '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5',
  'a9c43be948c5cabd56ef2bacffb77cdaa5eec49dd5eb0cc4129cf3eda5f0e74c',
  '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5',
  'c2eb7898bb6771503ffee5d0c722e5b561fe480edbc30141880a1cdf1e5b1cf6',
  'a92f6bdb75789bccc118adfcf704029aa58063c604bab4fcdd9cd126ef9b69af',
  '1c8bfe8f801d79745c4631d09fff36c82aa37fc4cce4fc946683d7b336b63032',
  'a01edad91c00abe7be5b72b5e36bf4ce3c6f26e8bce3340eba365642813ab8b6',
  'fc613b4dfd6736a7bd268c8a0e74ed0d1c04a959f59dd74ef2874983fd443fc9',
  '34550715062af006ac4fab288de67ecb44793c3a05c475227241535f6ef7a81b',
  '6382deaf1f5dc6e792b76db4a4a7bf2ba468884e000b25e7928e621e27fb23cb',
  '0bb09d80600eec3eb9d7793a6f859bedde2a2d83899b70bd78e961ed674b32f4',
  '000c285457fc971f862a79b786476c78812c8897063c6fa9c045f579a3b2d63f',
  '6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090',
  'd74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1',
  '136c67657614311f32238751044a0a3c0294f2a521e573afa8e496992d3786ba',
  '37bfdcb4c50793a6286fa0efe07b9e6bba8605b2c32e329fb9f71f225545f027',
  'dbc4a04327176e6577b4da46df04564150053960eba5d89587dad1f76a818d80',
  '9ce8db922a8f4a7abd859adee70bd8b7a63321265487da54cf4bed6a69eb3e1b',
  'e9a63a4eb15738ae85cd416221c8fcc4ccc0018fac91335b42eaa016c76e87f9',
  '81a83544cf93c245178cbc1620030f1123f435af867c79d87135983c52ab39d9',
  '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
  '1532e76dbe9d43d0dea98c331ca5ae8a65c5e8e8b99d3e2a42ae989356f6242a',
  '203b70b5ae883932161bbd0bded9357e763e63afce98b16230be33f0b94c2cc5',
  'd38681074467c0bc147b17a9a12b9efa8cc10bcf545f5b0bccccf5a93c4a2b79',
  'abc529a4b673cbbbc532e584706cb8137be876ad53269df3b97fbd40fc76fe57',
  '4007d46292298e83da10d0763d95d5139fe0c157148d0587aa912170414ccba6',
  'a0561fd649cdb6baa784055f051bad796ea0afef17fca38219549deeba4e8c1a',
  '686f746a95b6f836d7d70567c302c3f9ebb5ee0def3d1220ee9d4e9f34f5e131',
  'cbeaff314ef5ad032caa60ee2e8d8144ae52a8572c7d6f75631f3bd4080a7b16',
  '8bb0cf6eb9b17d0f7d22b456f121257dc1254e1f01665370476383ea776df414',
  '8f27f432fcbaa4b5180a1cc7a8fa166a93cda3c1bce6f19922dd519d02f4bb39',
  '308738b8195da46d65c96f4ee3909032e27c818d8a079bccb5a1ef62e8daaa45',
  'ed45d626b07112a8a501d9672f3b92796a6754b8d8d9cb4c617fec9774889220',
  '0522a55e2d5f0993a3d66d28864b2862a7218a75ea7968b075333434404485c3',
  'd979885447a413abb6d606a5d0f45c3b7809e6fde2c83f0df3426f1fc9bfed97',
  'b9dd960c1753459a78115d3cb845a57d924b6877e805b08bd01086ccdf34433c',
  '73cd1b16c4fb83061ad18a0b29b9643a68d4640075a466dc9e51682f84a847f5',
  'fa2115f8d576a6ab722956697fc759c31d1cd6b93c8336bfebf73ed5cba2ff49'
]

# Create a function which will hash a string
def hash_a_pass(password):
  
  # Create a hash object of the password using sha256
  sha256_password = hashlib.sha256(password.encode())

  # Return the hashed password
  return sha256_password

# Ask the user to input their password (TRY: "password" or "1234")
user_password = input("Please enter your password: ")

# Hash and store the user's password using the hash_a_pass() function
hashed_user_pass = hash_a_pass(user_password)

# Loop through all of the hashed passwords in the hashed_passes list
for password in hashed_passes:

  # Check if the hashed_user_pass is the same as the current password in the list
  if(str(hashed_user_pass.hexdigest()) == password):

    # Print out "LOGIN SUCCESSFUL!"
    print("Login Successful!")