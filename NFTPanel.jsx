import React, { useEffect, useState } from "react";

export default function NFTPanel() {
  const [nfts, setNfts] = useState([]);
  const [minting, setMinting] = useState(false);

  useEffect(() => {
    fetch("/api/nft/stats")
      .then((res) => res.json())
      .then((data) => setNfts(data.top_watched_nfts || []));
  }, []);

  const mintNFT = async () => {
    setMinting(true);
    await fetch("/api/nft/mint", { method: "POST" });
    setMinting(false);
  };

  return (
    <div className="bg-neutral-900 p-4 rounded border border-yellow-700 shadow-lg">
      <h2 className="text-xl text-yellow-400 font-bold mb-3">Memory Artifacts (NFT Vault)</h2>
      <button
        className="bg-yellow-500 hover:bg-yellow-600 text-black font-semibold py-2 px-4 rounded mb-4"
        onClick={mintNFT}
        disabled={minting}
      >
        {minting ? "Minting..." : "Mint NFT"}
      </button>
      <ul className="mt-4">
        {nfts.length === 0 ? (
          <li className="text-neutral-400">No NFTs found.</li>
        ) : (
          nfts.map((nft, idx) => (
            <li key={idx} className="mb-2">
              <span className="font-semibold">{nft.name || nft.id || `NFT #${idx + 1}`}</span>
              {nft.floor_price && (
                <span className="ml-2 text-yellow-300">Floor: {nft.floor_price}</span>
              )}
            </li>
          ))
        )}
      </ul>
    </div>
  );
}