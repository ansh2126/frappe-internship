const button = document.getElementById("loadBtn");
const results = document.getElementById("results");

button.addEventListener("click", async () => {
    results.innerHTML = "Loading Indian users...";

    try {
        const response = await fetch(
            "https://randomuser.me/api/?results=20&nat=IN"
        );

        const data = await response.json();

        results.innerHTML = "";

        data.results.forEach(user => {
            const card = document.createElement("div");

            card.className = "card";

            card.innerHTML = `
                <h2>${user.name.title} ${user.name.first} ${user.name.last}</h2>
                <p><strong>Email:</strong> ${user.email}</p>
                <p><strong>Phone:</strong> ${user.phone}</p>
                <p><strong>City:</strong> ${user.location.city}</p>
                <p><strong>State:</strong> ${user.location.state}</p>
                <p><strong>Country:</strong> ${user.location.country}</p>
            `;

            results.appendChild(card);
        });

    } catch (error) {
        results.innerHTML = "Failed to load users.";
        console.error(error);
    }
});
