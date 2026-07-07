"use client";

import { useParams } from "next/navigation";

export default function Page() {
  const { name } = useParams<{ name: string }>();

  return (
    <div>
      <h1>Login Page</h1>
      <p>Welcome, {name}!</p>
    </div>
  );
}