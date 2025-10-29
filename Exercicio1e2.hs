main :: IO () 
main = do{
    putStrLn "Digite o numero de linhas do triangulo de pascal"
    numero <- getLine
    let n = read numero :: Int
    let i = 0
    while i < n do
        let j = 0
        let valor = 1
        while j<=i do
            while j <= i do
                putStrLn valor ++ " "
                valor = valor * (i - j) / (j + 1)
                j = j + 1
                end
            end
        putStrLn "/n"
        i = i + 1
        end
    putStrLn "Digite o primeiro lado do triangulo:"
    aInput <- getLine
    putStrLn "Digite o segundo lado do triangulo:"
    bInput <- getLine
    putStrLn "Digite o terceiro lado do triangulo:"
    cInput <- getLine
    let a = read aInput :: Double
    let b = read bInput :: Double
    let c = read cInput :: Double
    if a <= 0 || b <= 0 || c <= 0 then
        putStrLn "Erro: todos os lados devem ser positivos."
    
    else if a + b <= c || a + c <= b || b + c <= a then
        putStrLn "Medidas invalidas — nao formam um triangulo."
    
    else if a == b && b == c then
        putStrLn "Triangulo equilatero valido."
    
    else if a == b || a == c || b == c then
        putStrLn "Triangulo isosceles valido."
    
    else
        putStrLn "Triangulo escaleno valido."
    
}