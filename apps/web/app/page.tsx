import styles from "./page.module.css";
import { readRootGet } from "../src/client/";
import Chat from "./components/Chat";


// Server Component to fetch backend data
async function BackendHello() {
  let data: string | null = null;
  let error: string | null = null;
  try {
    const res = await fetch("http://localhost:8900/", { cache: "no-store" });
    if (!res.ok) throw new Error("Network response was not ok");
    const json = await res.json();
    data = json.Hello;
  } catch (err: any) {
    error = err.message;
  }
  if (error) return <div>Error: {error}</div>;
  if (!data) return <div>Loading backend data...</div>;
  return <div>Simple fetch from backend says: <b>{data}</b></div>;
}

async function BackendHello2() {
  const { data } = await readRootGet();
  return <div>Generated client says: <b>{data?.Hello}</b></div>;
}

export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <BackendHello />
        <BackendHello2 />
        <Chat />
      </main>
    </div>
  );
}
