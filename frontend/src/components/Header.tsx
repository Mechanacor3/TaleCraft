import React, { useEffect, useState } from "react";

const Header: React.FC = () => {
  const [collapsed, setCollapsed] = useState<boolean>(() => {
    if (typeof window !== "undefined") {
      return localStorage.getItem("headerCollapsed") === "true";
    }
    return false;
  });

  useEffect(() => {
    localStorage.setItem("headerCollapsed", collapsed.toString());
  }, [collapsed]);

  return (
    <header className={`bg-blue-600 text-white ${collapsed ? "p-2" : "p-4"}`}>
      <div className="flex items-center">
        <button
          className="mr-2 focus:outline-none text-2xl"
          onClick={() => setCollapsed((c) => !c)}
          aria-label="Toggle header"
        >
          ☰
        </button>
        {!collapsed && (
          <div>
            <h1 className="text-2xl font-bold">ShortVideo Story Creator</h1>
            <p className="mt-2">
              Create engaging stories for your short videos!
            </p>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;
