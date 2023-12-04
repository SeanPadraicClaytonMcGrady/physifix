const URL = "http://localhost:8000";

export async function loginUser(username: string, password: string) {
  const response = await fetch(`${URL}/login`, {
    method: "POST",
    body: JSON.stringify({
      username,
      password,
    }),
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include",
  });

  if (response.status !== 200) {
    throw new Error("Incorrect credentials. Try again, or sign up.");
  }

  const login = await response.json();

  return login;
}
