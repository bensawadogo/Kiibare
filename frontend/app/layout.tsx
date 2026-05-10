import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Kiibare | Africa Market Access Intelligence",
  description: "The intelligent market access layer for African investors.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="fr">
      <body className={inter.className}>
        <nav className="bg-brand-dark text-white p-4 shadow-md">
          <div className="max-w-7xl mx-auto flex justify-between items-center">
            <h1 className="text-xl font-bold tracking-wider text-brand-accent">KIIBARE</h1>
            <div className="space-x-4">
              <button className="hover:text-brand-accent transition">Apprendre</button>
              <button className="hover:text-brand-accent transition">Marchés</button>
              <button className="bg-brand-primary px-4 py-2 rounded-md hover:bg-blue-700 transition">Connexion</button>
            </div>
          </div>
        </nav>
        <main className="min-h-screen">
          {children}
        </main>
      </body>
    </html>
  );
}
