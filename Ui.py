import streamlit as st

st.set_page_config(
    page_title="Python Exercise Learning Hub",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------- Content ---------------------------------
EXERCISES = [
    {
        "id": "2-1",
        "title": "Variables",
        "question": "Assign a message to a variable, then print that message.",
        "parts": [
            {
                "heading": "Part 1 — Store a message",
                "question": "Create a variable named message and store a sentence in it.",
                "code": 'message = "i am gonna be most rich people in my entire bloodline"',
                "explain_en": "A variable is a named place where Python keeps a value. Here, the variable message stores a string (text).",
                "explain_hi": "Variable ek named container jaisa hota hai jisme value store hoti hai. Yahan message variable ke andar text store hai.",
            },
            {
                "heading": "Part 2 — Print the message",
                "question": "Display the value stored inside message.",
                "code": "print(message)",
                "explain_en": "print() displays the value of the variable on the screen. You do not need quotation marks around message because you want the variable's value.",
                "explain_hi": "print() variable ke andar rakhi value ko screen par dikhata hai. message ko quotes mein nahi likhna, warna Python variable ki value ke bajay literal word print karega.",
            },
        ],
    },
    {
        "id": "2-2",
        "title": "Simple Messages",
        "question": "Assign a message to a variable and print it. Change the variable's value to a new message, then print it again.",
        "parts": [
            {
                "heading": "Part 1 — First value",
                "question": "Store your first message in message and print it.",
                "code": 'message = "i am gonna be most rich people in my entire bloodline"\\nprint(message)',
                "explain_en": "First, message refers to the first string. print(message) displays that string.",
                "explain_hi": "Pehle message variable mein first text store hota hai. print(message) us text ko display karta hai.",
            },
            {
                "heading": "Part 2 — Change the value",
                "question": "Assign a different message to the same variable and print it again.",
                "code": 'message = "i am gonna be the richest person in this country"\\nprint(message)',
                "explain_en": "Assigning a new value replaces the old value stored in message. The variable name stays the same; its value changes.",
                "explain_hi": "Same variable ko dobara value dene par purani value replace ho jaati hai. Variable ka naam same rehta hai, sirf value change hoti hai.",
            },
        ],
    },
    {
        "id": "2-3",
        "title": "Personal Message",
        "question": "Use a variable to represent a person's name. Print a message addressed to that person, such as: Hello Eric, would you like to learn some Python today?",
        "parts": [
            {
                "heading": "Part 1 — Store the name",
                "question": "Create a variable for a person's name.",
                "code": 'friend = "shazan"',
                "explain_en": "The variable friend stores the person's name as a string.",
                "explain_hi": "friend variable mein person ka naam string ke roop mein store kiya gaya hai.",
            },
            {
                "heading": "Part 2 — Personalize the message",
                "question": "Use an f-string to place the name inside your greeting.",
                "code": 'print(f"Hello {friend.title()}, hope you are good!")',
                "explain_en": "An f-string lets you insert a variable inside text using curly braces. title() capitalizes the first letter of each word.",
                "explain_hi": "f-string ki madad se text ke andar variable ki value curly braces {} mein daal sakte ho. title() naam ko Title Case mein karta hai.",
            },
        ],
    },
    {
        "id": "2-4",
        "title": "Name Cases",
        "question": "Store a person's name in a variable. Print the name in lowercase, uppercase, and title case.",
        "parts": [
            {
                "heading": "Part 1 — Store the name",
                "question": "Create a variable containing a name.",
                "code": 'friend = "shazan"',
                "explain_en": "The name is stored once, so you can reuse it with different string methods.",
                "explain_hi": "Naam ek hi variable mein store hai. Ab isi variable par alag-alag string methods use kar sakte ho.",
            },
            {
                "heading": "Part 2 — Use three case methods",
                "question": "Print the name in title case, uppercase, and lowercase.",
                "code": 'print(friend.title())\\nprint(friend.upper())\\nprint(friend.lower())',
                "explain_en": "title() capitalizes each word, upper() makes all letters uppercase, and lower() makes all letters lowercase.",
                "explain_hi": "title() har word ka pehla letter capital karta hai, upper() saare letters capital aur lower() saare letters small karta hai.",
            },
        ],
    },
    {
        "id": "2-5",
        "title": "Famous Quote",
        "question": "Find a quote from a famous person. Print the person's name and quote, including quotation marks around the quote.",
        "parts": [
            {
                "heading": "Part 1 — Print the attribution and quote",
                "question": "Use backslash-escaped double quotes so quotation marks appear in the output.",
                "code": 'print("Albert Einstein once said, \\\\"A person who never made a mistake never tried anything new.\\\\"")',
                "explain_en": 'The backslash (\\\\) is an escape character. It tells Python that the double quote is part of the text, not the end of the string.',
                "explain_hi": 'Backslash (\\\\) escape character hai. Ye Python ko batata hai ki double quote text ka hissa hai, string ko close nahi kar raha.',
            },
        ],
    },
    {
        "id": "2-6",
        "title": "Famous Quote 2 / Whitespace",
        "question": "Store a person's name with whitespace at the beginning and end. Use tab and newline characters at least once. Print the original value, then print it using lstrip(), rstrip(), and strip().",
        "parts": [
            {
                "heading": "Part 1 — Add whitespace",
                "question": "Store a name with a tab (\\\\t), newline (\\\\n), and spaces.",
                "code": 'name = "\\\\t\\\\n  daksh  \\\\n\\\\t"',
                "explain_en": "\\\\t adds a tab and \\\\n starts a new line. Spaces are also whitespace characters.",
                "explain_hi": "\\\\t tab space add karta hai aur \\\\n new line shuru karta hai. Normal spaces bhi whitespace hote hain.",
            },
            {
                "heading": "Part 2 — Display the original value",
                "question": "Print the name so you can inspect the whitespace.",
                "code": 'print("Original:", repr(name))',
                "explain_en": "repr() shows special characters such as tabs and newlines visibly, using escape notation. It helps you inspect the string.",
                "explain_hi": "repr() tab aur newline jaise special characters ko \\\\t aur \\\\n ke form mein dikhata hai, jisse whitespace samajhna easy hota hai.",
            },
            {
                "heading": "Part 3 — Strip whitespace",
                "question": "Use each of the three stripping methods.",
                "code": 'print("Left strip:", repr(name.lstrip()))\\nprint("Right strip:", repr(name.rstrip()))\\nprint("Full strip:", repr(name.strip()))',
                "explain_en": "lstrip() removes whitespace from the left, rstrip() removes it from the right, and strip() removes it from both ends. They do not remove whitespace from the middle.",
                "explain_hi": "lstrip() left side ka whitespace hatata hai, rstrip() right side ka, aur strip() dono sides ka. Beech ka whitespace remove nahi hota.",
            },
        ],
    },
    {
        "id": "2-7",
        "title": "Removing File Extensions",
        "question": "Store python_notes.txt in a variable named file_name. Use removesuffix() to display the filename without its extension.",
        "parts": [
            {
                "heading": "Part 1 — Store the filename",
                "question": "Create the file_name variable.",
                "code": 'file_name = "python_notes.txt"',
                "explain_en": "The full filename, including its extension, is stored as a string.",
                "explain_hi": "Poora filename extension ke saath ek string ke roop mein store hota hai.",
            },
            {
                "heading": "Part 2 — Remove the suffix",
                "question": "Remove .txt from the end of the filename.",
                "code": 'print(file_name.removesuffix(".txt"))',
                "explain_en": "removesuffix() removes the exact ending you provide if the string ends with it. Here it removes .txt.",
                "explain_hi": "removesuffix() string ke end se wahi suffix remove karta hai jo tum dete ho. Yahan .txt remove hota hai.",
            },
        ],
    },
    {
        "id": "2-8",
        "title": "Number Eight",
        "question": "Write addition, subtraction, multiplication, and division operations that each result in the number 8.",
        "parts": [
            {
                "heading": "Part 1 — Addition and subtraction",
                "question": "Write two expressions that result in 8.",
                "code": "print(5 + 3)\\nprint(9 - 1)",
                "explain_en": "Python evaluates the arithmetic expression first, then print() displays the result.",
                "explain_hi": "Python pehle mathematical calculation karta hai, phir print() answer display karta hai.",
            },
            {
                "heading": "Part 2 — Multiplication and division",
                "question": "Write two more expressions that result in 8.",
                "code": "print(16 / 2)\\nprint(4 * 2)",
                "explain_en": "The / operator performs division and * performs multiplication. In Python, 16 / 2 displays 8.0 because / returns a float.",
                "explain_hi": "/ division karta hai aur * multiplication. Python mein 16 / 2 ka result 8.0 aata hai, kyunki / float result deta hai.",
            },
        ],
    },
    {
        "id": "2-9",
        "title": "Favorite Number",
        "question": "Use a variable to represent your favorite number. Create a message that reveals your favorite number and print it.",
        "parts": [
            {
                "heading": "Part 1 — Store your favorite number",
                "question": "Create a variable and assign your favorite number.",
                "code": "favourite_number = 1",
                "explain_en": "The variable stores an integer because 1 is a whole number.",
                "explain_hi": "Variable mein integer store hai, kyunki 1 ek whole number hai.",
            },
            {
                "heading": "Part 2 — Reveal it in a message",
                "question": "Use an f-string to print a sentence containing the number.",
                "code": 'print(f"My favourite number is {favourite_number}")',
                "explain_en": "The f-string inserts the value of favourite_number into the message.",
                "explain_hi": "f-string favourite_number ki value ko sentence ke andar insert karta hai.",
            },
        ],
    },
    {
        "id": "3-1",
        "title": "Names",
        "question": "Store the names of a few friends in a list called names. Print each person's name by accessing each element in the list one at a time.",
        "parts": [
            {
                "heading": "Part 1 — Create the list",
                "question": "Store your friends' names in a list called names.",
                "code": 'names = ["shazan", "avaya", "ayush", "aman"]',
                "explain_en": "A list stores multiple values in one variable. Each item has an index, starting at 0.",
                "explain_hi": "List ek variable mein multiple values store karti hai. Har item ka index hota hai jo 0 se start hota hai.",
            },
            {
                "heading": "Part 2 — Access each item",
                "question": "Print each name using its index.",
                "code": "print(names[0])\\nprint(names[1])\\nprint(names[2])\\nprint(names[3])",
                "explain_en": "names[0] accesses the first item, names[1] the second, and so on. Python list indexes start at zero.",
                "explain_hi": "names[0] first item, names[1] second item ko access karta hai. Python mein indexing 0 se start hoti hai.",
            },
        ],
    },
    {
        "id": "3-2",
        "title": "Greetings",
        "question": "Use the list from the previous exercise. Instead of just printing each name, print the same personalized message to each person.",
        "parts": [
            {
                "heading": "Part 1 — Reuse the names list",
                "question": "Use the names list from Exercise 3-1.",
                "code": 'names = ["shazan", "avaya", "ayush", "aman"]',
                "explain_en": "You can reuse a list from an earlier exercise. You do not need to create a different list if the names are the same.",
                "explain_hi": "Pichhle exercise wali list dobara use kar sakte ho. Agar names same hain toh nayi list banana zaroori nahi.",
            },
            {
                "heading": "Part 2 — Personalize each greeting",
                "question": "Print the same greeting for each friend, inserting their name.",
                "code": 'print(f"Welcome my dear friend {names[0]}")\\nprint(f"Welcome my dear friend {names[1]}")\\nprint(f"Welcome my dear friend {names[2]}")\\nprint(f"Welcome my dear friend {names[3]}")',
                "explain_en": "The message stays the same, but the index changes, so each friend receives a greeting with their own name.",
                "explain_hi": "Message same rehta hai, lekin index change hota hai. Isliye har friend ko uske apne naam ke saath greeting milti hai.",
            },
        ],
    },
    {
        "id": "3-3",
        "title": "Your Own List",
        "question": "Think of your favorite mode of transportation, such as a motorcycle or car. Make a list and print statements about each item, such as 'I would like to own a motorcycle.'",
        "parts": [
            {
                "heading": "Part 1 — Create a transportation list",
                "question": "Make a list of vehicles you like.",
                "code": 'motorcycle = ["honda", "ducati", "bmw"]',
                "explain_en": "The list stores three transportation choices. The variable name can be any valid Python name.",
                "explain_hi": "List mein tumhari pasand ke teen vehicles store hain. Variable ka naam koi bhi valid Python name ho sakta hai.",
            },
            {
                "heading": "Part 2 — Print a statement for each item",
                "question": "Use each index in a personalized sentence.",
                "code": 'print(f"I would like to own {motorcycle[0]}")\\nprint(f"I would like to own {motorcycle[1]}")\\nprint(f"I would like to own {motorcycle[2]}")',
                "explain_en": "Each f-string inserts one item from the list into the sentence.",
                "explain_hi": "Har f-string list ke ek item ko sentence mein insert karta hai.",
            },
        ],
    },
    {
        "id": "3-4",
        "title": "Guest List",
        "question": "Make a list of at least three people you would like to invite to dinner. Print a personal invitation message to each person.",
        "parts": [
            {
                "heading": "Part 1 — Create the guest list",
                "question": "Choose at least three guests and store their names in a list.",
                "code": 'guests = ["Albert Einstein", "Elon Musk", "A.P.J. Abdul Kalam"]',
                "explain_en": "The guests list stores three names. A list is useful because you can add, replace, and remove guests later.",
                "explain_hi": "guests list mein teen names store hain. List useful hai kyunki baad mein guests add, replace aur remove kar sakte ho.",
            },
            {
                "heading": "Part 2 — Send invitations",
                "question": "Print one invitation for every guest using their index.",
                "code": 'print(f"Dear {guests[0]}, you are invited to dinner!")\\nprint(f"Dear {guests[1]}, you are invited to dinner!")\\nprint(f"Dear {guests[2]}, you are invited to dinner!")',
                "explain_en": "Each line accesses a different list item and inserts that guest's name into the invitation.",
                "explain_hi": "Har line list ke alag item ko access karti hai aur us guest ka naam invitation mein daalti hai.",
            },
        ],
    },
    {
        "id": "3-5",
        "title": "Changing Guest List",
        "question": "One invited guest cannot make it. Print their name, replace them with a new guest, and print a new invitation to each person still on the list.",
        "parts": [
            {
                "heading": "Part 1 — Replace the unavailable guest",
                "question": "Tell the user who cannot attend, then replace that person's name.",
                "code": 'print(f"Unfortunately, {guests[0]} cannot make it.")\\nguests[0] = "Shera bhai"',
                "explain_en": "guests[0] selects the first guest. Assigning a new name at that index replaces the old name.",
                "explain_hi": "guests[0] first guest ko select karta hai. Usi index par naya naam assign karne se purana naam replace ho jaata hai.",
            },
            {
                "heading": "Part 2 — Send invitations again",
                "question": "Print a fresh invitation for each guest after the replacement.",
                "code": 'print(f"Dear {guests[0]}, you are invited to dinner!")\\nprint(f"Dear {guests[1]}, you are invited to dinner!")\\nprint(f"Dear {guests[2]}, you are invited to dinner!")',
                "explain_en": "The list now contains the replacement guest, so the new invitations use the updated names.",
                "explain_hi": "Ab list mein replacement guest ka naam hai, isliye naye invitations updated names use karenge.",
            },
        ],
    },
    {
        "id": "3-6",
        "title": "More Guests",
        "question": "You found a bigger dinner table. Announce the good news, use insert() to add one guest at the beginning and another in the middle, use append() to add one at the end, then invite everyone.",
        "parts": [
            {
                "heading": "Part 1 — Announce the bigger table",
                "question": "Print a message telling everyone that you found a bigger table.",
                "code": 'print("Good news! I found a bigger dinner table.")',
                "explain_en": "This is just a message to announce that you can invite more people.",
                "explain_hi": "Ye message batata hai ki ab tumhare paas zyada guests ko invite karne ki jagah hai.",
            },
            {
                "heading": "Part 2 — Add guests with insert() and append()",
                "question": "Add one person at the start, one in the middle, and one at the end.",
                "code": 'guests.insert(0, "Ada Lovelace")\\nguests.insert(2, "Alan Turing")\\nguests.append("Leonardo da Vinci")',
                "explain_en": "insert(index, value) adds an item at a chosen position. append(value) adds an item to the end of the list.",
                "explain_hi": "insert(index, value) chosen position par item add karta hai. append(value) list ke end mein item add karta hai.",
            },
            {
                "heading": "Part 3 — Invite all six guests",
                "question": "Print an invitation for every guest in the updated list.",
                "code": 'print(f"Dear {guests[0]}, you are invited!")\\nprint(f"Dear {guests[1]}, you are invited!")\\nprint(f"Dear {guests[2]}, you are invited!")\\nprint(f"Dear {guests[3]}, you are invited!")\\nprint(f"Dear {guests[4]}, you are invited!")\\nprint(f"Dear {guests[5]}, you are invited!")',
                "explain_en": "There are now six guests. Each index from 0 through 5 accesses one guest.",
                "explain_hi": "Ab list mein 6 guests hain. Index 0 se 5 tak har guest ko access karta hai.",
            },
        ],
    },
    {
        "id": "3-7",
        "title": "Shrinking Guest List",
        "question": "The bigger table will not arrive in time, so you can invite only two people. Announce this, use pop() to remove guests one at a time and apologize each time, tell the remaining two they are still invited, use del to remove the last two names, and print the empty list.",
        "parts": [
            {
                "heading": "Part 1 — Announce the change",
                "question": "Print a message explaining that only two people can be invited.",
                "code": 'print("The table will not arrive in time. I can invite only two people.")',
                "explain_en": "This message explains why the guest list needs to become smaller.",
                "explain_hi": "Ye message batata hai ki guest list chhoti kyun karni hai: ab sirf do log invite ho sakte hain.",
            },
            {
                "heading": "Part 2 — Remove guests one at a time",
                "question": "Use pop() four times. After each pop, immediately print an apology to the person who was removed.",
                "code": 'removed_guest = guests.pop()\\nprint(f"Sorry {removed_guest}, I cannot invite you to dinner.")\\n\\nremoved_guest = guests.pop()\\nprint(f"Sorry {removed_guest}, I cannot invite you to dinner.")\\n\\nremoved_guest = guests.pop()\\nprint(f"Sorry {removed_guest}, I cannot invite you to dinner.")\\n\\nremoved_guest = guests.pop()\\nprint(f"Sorry {removed_guest}, I cannot invite you to dinner.")',
                "explain_en": "pop() removes and returns an item. With no index given, it removes the last item. Store the returned name so you can apologize to that person.",
                "explain_hi": "pop() item ko remove bhi karta hai aur return bhi. Index na do toh last item remove hota hai. Returned naam variable mein rakho taaki us person ko sorry bol sako.",
            },
            {
                "heading": "Part 3 — Confirm the remaining two guests",
                "question": "Print a message to each of the two guests who are still on the list.",
                "code": 'print(f"Dear {guests[0]}, you are still invited!")\\nprint(f"Dear {guests[1]}, you are still invited!")',
                "explain_en": "After removing four guests from a list of six, two guests remain. Their indexes are 0 and 1.",
                "explain_hi": "Six guests mein se four remove karne ke baad two guests bachenge. Unke indexes 0 aur 1 hain.",
            },
            {
                "heading": "Part 4 — Empty the list",
                "question": "Use del to remove the remaining names, then print the list.",
                "code": 'del guests[0]\\ndel guests[0]\\nprint(guests)',
                "explain_en": "After deleting index 0, the second guest shifts into index 0. Delete index 0 again. The final print should display an empty list: [].",
                "explain_hi": "Pehla index 0 delete karne ke baad doosra guest bhi index 0 par aa jaata hai. Isliye dobara guests[0] delete karo. Final output [] hona chahiye.",
            },
        ],
    },
]

# ----------------------------- Styling ----------------------------------
st.markdown(
    """
    <style>
    .block-container {padding-top: 1.7rem; padding-bottom: 3rem; max-width: 1150px;}
    .hero {
        padding: 1.35rem 1.5rem; border-radius: 18px;
        background: linear-gradient(115deg, rgba(99,102,241,.18), rgba(14,165,233,.10));
        border: 1px solid rgba(129,140,248,.28); margin-bottom: 1.1rem;
    }
    .muted {color: #9CA3AF; font-size: .92rem;}
    .part-card {
        padding: 1rem 1.1rem; border: 1px solid rgba(128,128,128,.25);
        border-radius: 14px; margin: .7rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------- Sidebar ----------------------------------
st.sidebar.title("🐍 Python Learning Hub")
st.sidebar.caption("Exercises 2-1 to 3-7")
language = st.sidebar.radio(
    "Explanation language / भाषा",
    ["Simple English", "Hinglish"],
    index=1,
)
st.sidebar.divider()
st.sidebar.subheader("Choose an exercise")

grouped = {
    "Chapter 2 — Variables & Strings": [e for e in EXERCISES if e["id"].startswith("2-")],
    "Chapter 3 — Lists": [e for e in EXERCISES if e["id"].startswith("3-")],
}

selected_id = None
for group_name, items in grouped.items():
    with st.sidebar.expander(group_name, expanded=(group_name.endswith("Strings"))):
        for exercise in items:
            label = f'{exercise["id"]} · {exercise["title"]}'
            if st.button(label, key=f'nav_{exercise["id"]}', use_container_width=True):
                st.session_state.selected_exercise = exercise["id"]

if "selected_exercise" not in st.session_state:
    st.session_state.selected_exercise = "2-1"

selected = next(
    (exercise for exercise in EXERCISES if exercise["id"] == st.session_state.selected_exercise),
    EXERCISES[0],
)

# ----------------------------- Main page --------------------------------
st.markdown(
    """
    <div class="hero">
      <h1 style="margin:0;">Learn Python, one exercise at a time 🐍</h1>
      <p style="margin:.45rem 0 0 0;">Questions, code broken into small parts, and explanations in simple English or Hinglish.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

total = len(EXERCISES)
done_ids = st.session_state.get("completed_exercises", [])
st.progress(len(done_ids) / total, text=f"Progress: {len(done_ids)} of {total} exercises marked complete")

col_a, col_b, col_c = st.columns(3)
col_a.metric("Current exercise", selected["id"])
col_b.metric("Parts in this exercise", len(selected["parts"]))
col_c.metric("Completed", f"{len(done_ids)}/{total}")

st.divider()
st.caption(f'CHAPTER {"2 · VARIABLES & STRINGS" if selected["id"].startswith("2-") else "3 · LISTS"}')
st.title(f'Exercise {selected["id"]}: {selected["title"]}')
st.subheader("Question")
st.write(selected["question"])

st.info(
    "Learning tip: Read the question first, try writing the code yourself, then open each part to compare and understand it. "
    "The guest-list examples use individual statements, not loops."
)

for index, part in enumerate(selected["parts"], start=1):
    with st.expander(part["heading"], expanded=(index == 1)):
        st.markdown(f"**What you need to do:** {part['question']}")
        st.markdown("**Example code**")
        st.code(part["code"].replace("\\n", "\n"), language="python")
        st.markdown("**Explanation**")
        if language == "Simple English":
            st.write(part["explain_en"])
        else:
            st.write(part["explain_hi"])

        if selected["id"] == "3-7" and index == 2:
            st.warning(
                "Important: The exercise says to apologize immediately after each pop(). "
                "Do not pop all four guests first and print all apologies afterward."
            )

st.divider()
done = selected["id"] in done_ids
if done:
    st.success("You marked this exercise as complete.")
else:
    if st.button("Mark this exercise complete ✓", type="primary"):
        st.session_state.completed_exercises = done_ids + [selected["id"]]
        st.rerun()

left, right = st.columns(2)
current_index = next(i for i, e in enumerate(EXERCISES) if e["id"] == selected["id"])
with left:
    if current_index > 0:
        previous = EXERCISES[current_index - 1]
        if st.button(f"← Previous: {previous['id']} {previous['title']}", use_container_width=True):
            st.session_state.selected_exercise = previous["id"]
            st.rerun()
with right:
    if current_index < len(EXERCISES) - 1:
        following = EXERCISES[current_index + 1]
        if st.button(f"Next: {following['id']} {following['title']} →", use_container_width=True):
            st.session_state.selected_exercise = following["id"]
            st.rerun()

st.sidebar.divider()
st.sidebar.caption("Made for beginner Python learners • No loop-based guest-list solutions")
