<!DOCTYPE html>
<html>
<body>

<h2>My AI</h2>

<input id="msg">
<button onclick="send()">Send</button>

<p id="chat"></p>

<!-- ✅ Payment button OUTSIDE script -->
<button onclick="pay()">Pay ₹50 to Continue</button>

<script>
async function send(){
 let m = document.getElementById("msg").value;

 let r = await fetch("/chat", {
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body: JSON.stringify({message:m})
 });

 let d = await r.json();
 document.getElementById("chat").innerHTML += "<br>You: "+m+"<br>AI: "+d.reply;
}

function pay() {
    alert("Payment system coming soon 🚀");
}
</script>

</body>
</html>
    app.run(host="0.0.0.0", port=10000)
