function test()
    s1 = "Hooray!"
    s2 = "Great!"
    print(s1," ", s2," Let's do some maths: ")

    function hiddenf(i, j)
        for i in 1:i, j in 1:j
            print(i * j, " ")
        end
        println("\n**\nCongratulations! You passed the setup test.\n** END")
    end

    return hiddenf, s1, s2
end



    
