import React, { useState } from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function HIERiskPredictor() {
  const [PHA, setPHA] = useState('');
  const [BEA, setBEA] = useState('');
  const [LATA, setLATA] = useState('');
  const [risk, setRisk] = useState(null);

  const calculateRisk = () => {
    const pha = parseFloat(PHA);
    const bea = parseFloat(BEA);
    const lata = parseFloat(LATA);

    // Coefficienti derivati dal modello calibrato (ipotetici per questa demo)
    const coefficients = { intercept: -4.5, PHA: 1.2, BEA: 0.8, LATA: 1.0 };

    // Calcolo della probabilità (logistic regression formula)
    const logit = coefficients.intercept + (coefficients.PHA * pha) + (coefficients.BEA * bea) + (coefficients.LATA * lata);
    const probability = 1 / (1 + Math.exp(-logit));

    // Soglia ottimale identificata dal punto di Youden
    const threshold = 0.0081;

    setRisk(probability >= threshold ? `Alto rischio di HIE (${(probability * 100).toFixed(2)}%)` : `Basso rischio di HIE (${(probability * 100).toFixed(2)}%)`);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <Card className="w-full max-w-md p-6">
        <CardContent>
          <h2 className="text-xl font-bold text-center mb-4">Calcolatore del Rischio HIE</h2>
          <div className="space-y-4">
            <Input type="number" placeholder="PHA" value={PHA} onChange={(e) => setPHA(e.target.value)} />
            <Input type="number" placeholder="BEA" value={BEA} onChange={(e) => setBEA(e.target.value)} />
            <Input type="number" placeholder="LATTATI" value={LATA} onChange={(e) => setLATA(e.target.value)} />
            <Button onClick={calculateRisk} className="w-full">Calcola Rischio</Button>
          </div>
          {risk && (
            <div className="mt-4 p-4 bg-gray-200 rounded text-center">
              <strong>Risultato:</strong>
              <p>{risk}</p>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
